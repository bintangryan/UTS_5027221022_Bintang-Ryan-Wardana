import grpc
import fainens_pb2
import fainens_pb2_grpc

def add_transaction(stub):
    transaction_id = input("Enter transaction ID: ")
    transaction_type = input("Enter transaction type (PEMASUKAN/PENGELUARAN): ").upper()
    amount = float(input("Enter amount: "))
    date = input("Enter date (Format: mm/dd/yy): ")
    description = input("Enter description: ")

    transaction = fainens_pb2.Transaction(
        id=transaction_id,
        type=fainens_pb2.Transaction.PEMASUKAN if transaction_type == "PEMASUKAN" else fainens_pb2.Transaction.PENGELUARAN,
        amount=amount,
        date=date,
        description=description
    )

    response = stub.AddTransaction(fainens_pb2.AddTransactionRequest(transaction=transaction))
    print("Transaction added successfully:", response.transaction)

def get_transactions_by_type(stub):
    transaction_type = input("Enter transaction type to filter (PEMASUKAN/PENGELUARAN): ").upper()

    response = stub.GetTransactionsByType(fainens_pb2.GetTransactionsByTypeRequest(
        type=fainens_pb2.Transaction.PEMASUKAN if transaction_type == "PEMASUKAN" else fainens_pb2.Transaction.PENGELUARAN
    ))

    print(f"Transactions of type {transaction_type}:")
    for transaction in response.transactions:
        print(transaction)

def update_transaction(stub):
    transaction_id = input("Enter ID of transaction to update: ")
    transaction_type = input("Enter new transaction type (PEMASUKAN/PENGELUARAN): ").upper()
    amount = float(input("Enter new amount: "))
    date = input("Enter new date (Format: mm/dd/yy): ")
    description = input("Enter new description: ")

    transaction = fainens_pb2.Transaction(
        id=transaction_id,
        type=fainens_pb2.Transaction.PEMASUKAN if transaction_type == "PEMASUKAN" else fainens_pb2.Transaction.PENGELUARAN,
        amount=amount,
        date=date,
        description=description
    )

    response = stub.UpdateTransaction(fainens_pb2.UpdateTransactionRequest(
        id=transaction_id,
        transaction=transaction
    ))

    if response.transaction:
        print("Transaction updated successfully:", response.transaction)
    else:
        print("Transaction not found")

def delete_transaction(stub):
    transaction_id = input("Enter ID of transaction to delete: ")

    response = stub.DeleteTransaction(fainens_pb2.DeleteTransactionRequest(id=transaction_id))

    print(response.message)

def run():
    channel = grpc.insecure_channel('localhost:5060')
    stub = fainens_pb2_grpc.TransactionServiceStub(channel)

    while True:
        print("\nMenu:")
        print("1. Add Transaction")
        print("2. Get Transactions by Type")
        print("3. Update Transaction")
        print("4. Delete Transaction")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            add_transaction(stub)
        elif choice == "2":
            get_transactions_by_type(stub)
        elif choice == "3":
            update_transaction(stub)
        elif choice == "4":
            delete_transaction(stub)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == '__main__':
    run()
