# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fainens.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rfainens.proto\"\xab\x01\n\x0bTransaction\x12\n\n\x02id\x18\x01 \x01(\t\x12*\n\x04type\x18\x02 \x01(\x0e\x32\x1c.Transaction.TransactionType\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x02\x12\x0c\n\x04\x64\x61te\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\"1\n\x0fTransactionType\x12\r\n\tPEMASUKAN\x10\x00\x12\x0f\n\x0bPENGELUARAN\x10\x01\":\n\x15\x41\x64\x64TransactionRequest\x12!\n\x0btransaction\x18\x01 \x01(\x0b\x32\x0c.Transaction\";\n\x16\x41\x64\x64TransactionResponse\x12!\n\x0btransaction\x18\x01 \x01(\x0b\x32\x0c.Transaction\"J\n\x1cGetTransactionsByTypeRequest\x12*\n\x04type\x18\x01 \x01(\x0e\x32\x1c.Transaction.TransactionType\"C\n\x1dGetTransactionsByTypeResponse\x12\"\n\x0ctransactions\x18\x01 \x03(\x0b\x32\x0c.Transaction\"I\n\x18UpdateTransactionRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12!\n\x0btransaction\x18\x02 \x01(\x0b\x32\x0c.Transaction\">\n\x19UpdateTransactionResponse\x12!\n\x0btransaction\x18\x01 \x01(\x0b\x32\x0c.Transaction\"&\n\x18\x44\x65leteTransactionRequest\x12\n\n\x02id\x18\x01 \x01(\t\",\n\x19\x44\x65leteTransactionResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\xc7\x02\n\x12TransactionService\x12\x41\n\x0e\x41\x64\x64Transaction\x12\x16.AddTransactionRequest\x1a\x17.AddTransactionResponse\x12V\n\x15GetTransactionsByType\x12\x1d.GetTransactionsByTypeRequest\x1a\x1e.GetTransactionsByTypeResponse\x12J\n\x11UpdateTransaction\x12\x19.UpdateTransactionRequest\x1a\x1a.UpdateTransactionResponse\x12J\n\x11\x44\x65leteTransaction\x12\x19.DeleteTransactionRequest\x1a\x1a.DeleteTransactionResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'fainens_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_TRANSACTION']._serialized_start=18
  _globals['_TRANSACTION']._serialized_end=189
  _globals['_TRANSACTION_TRANSACTIONTYPE']._serialized_start=140
  _globals['_TRANSACTION_TRANSACTIONTYPE']._serialized_end=189
  _globals['_ADDTRANSACTIONREQUEST']._serialized_start=191
  _globals['_ADDTRANSACTIONREQUEST']._serialized_end=249
  _globals['_ADDTRANSACTIONRESPONSE']._serialized_start=251
  _globals['_ADDTRANSACTIONRESPONSE']._serialized_end=310
  _globals['_GETTRANSACTIONSBYTYPEREQUEST']._serialized_start=312
  _globals['_GETTRANSACTIONSBYTYPEREQUEST']._serialized_end=386
  _globals['_GETTRANSACTIONSBYTYPERESPONSE']._serialized_start=388
  _globals['_GETTRANSACTIONSBYTYPERESPONSE']._serialized_end=455
  _globals['_UPDATETRANSACTIONREQUEST']._serialized_start=457
  _globals['_UPDATETRANSACTIONREQUEST']._serialized_end=530
  _globals['_UPDATETRANSACTIONRESPONSE']._serialized_start=532
  _globals['_UPDATETRANSACTIONRESPONSE']._serialized_end=594
  _globals['_DELETETRANSACTIONREQUEST']._serialized_start=596
  _globals['_DELETETRANSACTIONREQUEST']._serialized_end=634
  _globals['_DELETETRANSACTIONRESPONSE']._serialized_start=636
  _globals['_DELETETRANSACTIONRESPONSE']._serialized_end=680
  _globals['_TRANSACTIONSERVICE']._serialized_start=683
  _globals['_TRANSACTIONSERVICE']._serialized_end=1010
# @@protoc_insertion_point(module_scope)