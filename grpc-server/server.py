# server.py

import grpc
import logging
import pymongo
from flask import Flask, request, jsonify
import fainens_pb2
import fainens_pb2_grpc
from concurrent import futures

app = Flask(__name__)

# Dummy data to store transactions
transactions = []

class TransactionService(fainens_pb2_grpc.TransactionServiceServicer):
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")  # Connect to MongoDB
        self.db = self.client["Fainens"]  # Specify the database name
        self.collection = self.db["TransactionList"]  # Specify the collection name
        logging.info("Connected to MongoDB")

    def AddTransaction(self, request, context):
        logging.info("Received AddTransaction request: %s", request)
        transaction = request.transaction
        transaction_data = {
            "id": transaction.id,
            "type": transaction.type,
            "amount": transaction.amount,
            "date": transaction.date,
            "description": transaction.description
        }
        self.collection.insert_one(transaction_data)  # Insert transaction data into MongoDB
        return fainens_pb2.AddTransactionResponse(transaction=transaction)

    def GetTransactionsByType(self, request, context):
        logging.info("Received GetTransactionsByType request: %s", request)
        
        # Extract transaction type from request
        transaction_type = request.type
        
        # Convert transaction type from protobuf enum to MongoDB-compatible value
        # For example, if transaction_type is PEMASUKAN, we change it to 0, if PENGELUARAN, we change it to 1
        transaction_type_value = 0 if transaction_type == fainens_pb2.Transaction.PEMASUKAN else 1
        
        # Query MongoDB to get transactions with the matching type
        transactions_by_type = list(self.collection.find({"type": transaction_type_value}))
        
        # Convert MongoDB query result to list of protobuf Transaction objects
        transactions_proto = []
        for transaction_data in transactions_by_type:
            transaction = fainens_pb2.Transaction(
                id=transaction_data["id"],
                type=transaction_data["type"],
                amount=transaction_data["amount"],
                date=transaction_data["date"],
                description=transaction_data["description"]
            )
            transactions_proto.append(transaction)
        
        # Return response with list of protobuf transactions
        return fainens_pb2.GetTransactionsByTypeResponse(transactions=transactions_proto)


    def UpdateTransaction(self, request, context):
        logging.info("Received UpdateTransaction request: %s", request)
        transaction = request.transaction
        transaction_data = {
            "id": transaction.id,
            "type": transaction.type,
            "amount": transaction.amount,
            "date": transaction.date,
            "description": transaction.description
        }
        self.collection.update_one({"id": request.id}, {"$set": transaction_data})
        return fainens_pb2.UpdateTransactionResponse(transaction=transaction)

    def DeleteTransaction(self, request, context):
        logging.info("Received DeleteTransaction request: %s", request)
        self.collection.delete_one({"id": request.id})
        return fainens_pb2.DeleteTransactionResponse(message="Transaction deleted successfully")

# Initialize gRPC server
def serve():
    logging.basicConfig(level=logging.INFO)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    fainens_pb2_grpc.add_TransactionServiceServicer_to_server(TransactionService(), server)
    server.add_insecure_port('[::]:5060')
    server.start()
    logging.info("gRPC server is listening on port 5060")
    server.wait_for_termination()

# Endpoint for adding transaction via REST API
@app.route('/transactions', methods=['POST'])
def add_transaction():
    # Get transaction data from request body
    transaction_data = request.json

    # Create protobuf transaction object
    transaction = fainens_pb2.Transaction(
        id=transaction_data['id'],
        type=transaction_data['type'],  # Still using 'type' here
        amount=transaction_data['amount'],
        date=transaction_data['date'],
        description=transaction_data['description']
    )

    # Send transaction data to gRPC server
    try:
        with grpc.insecure_channel('localhost:5060') as channel:
            stub = fainens_pb2_grpc.TransactionServiceStub(channel)
            response = stub.AddTransaction(fainens_pb2.AddTransactionRequest(transaction=transaction))
            return jsonify({'message': 'Transaction added successfully'})
    except grpc.RpcError as e:
        # Handle gRPC errors
        return jsonify({'error': 'Failed to add transaction: ' + str(e)})

# Endpoint for getting transactions by type via REST API
@app.route('/transactions/<string:type>', methods=['GET'])
def get_transactions_by_type(type):
    # Send request to gRPC server to get transactions by type
    try:
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = fainens_pb2_grpc.TransactionServiceStub(channel)
            response = stub.GetTransactionsByType(fainens_pb2.GetTransactionsByTypeRequest(type=type))
            transactions = [{'id': transaction.id, 'type': transaction.type, 'amount': transaction.amount, 'date': transaction.date, 'description': transaction.description} for transaction in response.transactions]
            return jsonify(transactions)
    except grpc.RpcError as e:
        # Handle gRPC errors
        return jsonify({'error': 'Failed to get transactions: ' + str(e)})

# Endpoint for updating transaction via REST API
@app.route('/transactions/<string:id>', methods=['PUT'])
def update_transaction(id):
    # Get transaction data from request body
    transaction_data = request.json

    # Create protobuf transaction object
    transaction = fainens_pb2.Transaction(
        id=id,
        type=transaction_data['type'],  # Still using 'type' here
        amount=transaction_data['amount'],
        date=transaction_data['date'],
        description=transaction_data['description']
    )

    # Send transaction data to gRPC server for update
    try:
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = fainens_pb2_grpc.TransactionServiceStub(channel)
            response = stub.UpdateTransaction(fainens_pb2.UpdateTransactionRequest(id=id, transaction=transaction))
            return jsonify({'message': 'Transaction updated successfully'})
    except grpc.RpcError as e:
        # Handle gRPC errors
        return jsonify({'error': 'Failed to update transaction: ' + str(e)})

# Endpoint for deleting transaction via REST API
@app.route('/transactions/<string:id>', methods=['DELETE'])
def delete_transaction(id):
    # Send request to gRPC server for deletion
    try:
        with grpc.insecure_channel('localhost:5060') as channel:
            stub = fainens_pb2_grpc.TransactionServiceStub(channel)
            response = stub.DeleteTransaction(fainens_pb2.DeleteTransactionRequest(id=id))
            return jsonify({'message': response.message})
    except grpc.RpcError as e:
        # Handle gRPC errors
        return jsonify({'error': 'Failed to delete transaction: ' + str(e)})


if __name__ == '__main__' :
    serve()
