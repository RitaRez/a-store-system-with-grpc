# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bank.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nbank.proto\"%\n\x0f\x62\x61lance_request\x12\x12\n\nwallet_key\x18\x01 \x02(\t\"(\n\x0f\x62\x61lance_respose\x12\x15\n\rbalance_value\x18\x01 \x02(\x05\"4\n\x0fpayment_request\x12\x12\n\nwallet_key\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\x05\"5\n\x0fpayment_respose\x12\x0e\n\x06status\x18\x01 \x02(\x05\x12\x12\n\nauth_token\x18\x02 \x01(\x07\"I\n\x10transfer_request\x12\r\n\x05\x63\x61lue\x18\x01 \x02(\x05\x12\x12\n\nauth_token\x18\x02 \x01(\x07\x12\x12\n\nwallet_key\x18\x03 \x02(\t\"\"\n\x10transfer_respose\x12\x0e\n\x06status\x18\x01 \x02(\x05\"\x15\n\x13\x65nd_of_work_request\"%\n\x13\x65nd_of_work_respose\x12\x0e\n\x06status\x18\x01 \x02(\x05\x32\xd1\x01\n\x04\x42\x61nk\x12-\n\x07\x62\x61lance\x12\x10.balance_request\x1a\x10.balance_respose\x12-\n\x07payment\x12\x10.payment_request\x1a\x10.payment_respose\x12\x30\n\x08transfer\x12\x11.transfer_request\x1a\x11.transfer_respose\x12\x39\n\x0b\x65nd_of_work\x12\x14.end_of_work_request\x1a\x14.end_of_work_respose')



_BALANCE_REQUEST = DESCRIPTOR.message_types_by_name['balance_request']
_BALANCE_RESPOSE = DESCRIPTOR.message_types_by_name['balance_respose']
_PAYMENT_REQUEST = DESCRIPTOR.message_types_by_name['payment_request']
_PAYMENT_RESPOSE = DESCRIPTOR.message_types_by_name['payment_respose']
_TRANSFER_REQUEST = DESCRIPTOR.message_types_by_name['transfer_request']
_TRANSFER_RESPOSE = DESCRIPTOR.message_types_by_name['transfer_respose']
_END_OF_WORK_REQUEST = DESCRIPTOR.message_types_by_name['end_of_work_request']
_END_OF_WORK_RESPOSE = DESCRIPTOR.message_types_by_name['end_of_work_respose']
balance_request = _reflection.GeneratedProtocolMessageType('balance_request', (_message.Message,), {
  'DESCRIPTOR' : _BALANCE_REQUEST,
  '__module__' : 'bank_pb2'
  # @@protoc_insertion_point(class_scope:balance_request)
  })
_sym_db.RegisterMessage(balance_request)

balance_respose = _reflection.GeneratedProtocolMessageType('balance_respose', (_message.Message,), {
  'DESCRIPTOR' : _BALANCE_RESPOSE,
  '__module__' : 'bank_pb2'
  # @@protoc_insertion_point(class_scope:balance_respose)
  })
_sym_db.RegisterMessage(balance_respose)

payment_request = _reflection.GeneratedProtocolMessageType('payment_request', (_message.Message,), {
  'DESCRIPTOR' : _PAYMENT_REQUEST,
  '__module__' : 'bank_pb2'
  # @@protoc_insertion_point(class_scope:payment_request)
  })
_sym_db.RegisterMessage(payment_request)

payment_respose = _reflection.GeneratedProtocolMessageType('payment_respose', (_message.Message,), {
  'DESCRIPTOR' : _PAYMENT_RESPOSE,
  '__module__' : 'bank_pb2'
  # @@protoc_insertion_point(class_scope:payment_respose)
  })
_sym_db.RegisterMessage(payment_respose)

transfer_request = _reflection.GeneratedProtocolMessageType('transfer_request', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFER_REQUEST,
  '__module__' : 'bank_pb2'
  # @@protoc_insertion_point(class_scope:transfer_request)
  })
_sym_db.RegisterMessage(transfer_request)

transfer_respose = _reflection.GeneratedProtocolMessageType('transfer_respose', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFER_RESPOSE,
  '__module__' : 'bank_pb2'
  # @@protoc_insertion_point(class_scope:transfer_respose)
  })
_sym_db.RegisterMessage(transfer_respose)

end_of_work_request = _reflection.GeneratedProtocolMessageType('end_of_work_request', (_message.Message,), {
  'DESCRIPTOR' : _END_OF_WORK_REQUEST,
  '__module__' : 'bank_pb2'
  # @@protoc_insertion_point(class_scope:end_of_work_request)
  })
_sym_db.RegisterMessage(end_of_work_request)

end_of_work_respose = _reflection.GeneratedProtocolMessageType('end_of_work_respose', (_message.Message,), {
  'DESCRIPTOR' : _END_OF_WORK_RESPOSE,
  '__module__' : 'bank_pb2'
  # @@protoc_insertion_point(class_scope:end_of_work_respose)
  })
_sym_db.RegisterMessage(end_of_work_respose)

_BANK = DESCRIPTOR.services_by_name['Bank']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BALANCE_REQUEST._serialized_start=14
  _BALANCE_REQUEST._serialized_end=51
  _BALANCE_RESPOSE._serialized_start=53
  _BALANCE_RESPOSE._serialized_end=93
  _PAYMENT_REQUEST._serialized_start=95
  _PAYMENT_REQUEST._serialized_end=147
  _PAYMENT_RESPOSE._serialized_start=149
  _PAYMENT_RESPOSE._serialized_end=202
  _TRANSFER_REQUEST._serialized_start=204
  _TRANSFER_REQUEST._serialized_end=277
  _TRANSFER_RESPOSE._serialized_start=279
  _TRANSFER_RESPOSE._serialized_end=313
  _END_OF_WORK_REQUEST._serialized_start=315
  _END_OF_WORK_REQUEST._serialized_end=336
  _END_OF_WORK_RESPOSE._serialized_start=338
  _END_OF_WORK_RESPOSE._serialized_end=375
  _BANK._serialized_start=378
  _BANK._serialized_end=587
# @@protoc_insertion_point(module_scope)
