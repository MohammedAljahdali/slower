# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: server_model.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12server_model.proto\x12\x0cserver_model\"\xc4\x01\n\tBatchData\x12\x0e\n\x06method\x18\x01 \x01(\t\x12/\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32!.server_model.BatchData.DataEntry\x12/\n\x0c\x63ontrol_code\x18\x03 \x01(\x0e\x32\x19.server_model.ControlCode\x1a\x45\n\tDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.server_model.ByteTensor:\x02\x38\x01\"Z\n\nByteTensor\x12\x17\n\rsingle_tensor\x18\x01 \x01(\x0cH\x00\x12+\n\x07tensors\x18\x02 \x01(\x0b\x32\x18.server_model.TensorListH\x00\x42\x06\n\x04\x64\x61ta\"\x1d\n\nTensorList\x12\x0f\n\x07tensors\x18\x01 \x03(\x0c*]\n\x0b\x43ontrolCode\x12\x06\n\x02OK\x10\x00\x12\x13\n\x0f\x44O_CLOSE_STREAM\x10\x01\x12\x14\n\x10STREAM_CLOSED_OK\x10\x02\x12\x1b\n\x17\x45RROR_PROCESSING_STREAM\x10\x03\x32\x9f\x01\n\x0bServerModel\x12\x45\n\x0f\x42lockingRequest\x12\x17.server_model.BatchData\x1a\x17.server_model.BatchData\"\x00\x12I\n\x11StreamingRequests\x12\x17.server_model.BatchData\x1a\x17.server_model.BatchData\"\x00(\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'server_model_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_BATCHDATA_DATAENTRY']._options = None
  _globals['_BATCHDATA_DATAENTRY']._serialized_options = b'8\001'
  _globals['_CONTROLCODE']._serialized_start=358
  _globals['_CONTROLCODE']._serialized_end=451
  _globals['_BATCHDATA']._serialized_start=37
  _globals['_BATCHDATA']._serialized_end=233
  _globals['_BATCHDATA_DATAENTRY']._serialized_start=164
  _globals['_BATCHDATA_DATAENTRY']._serialized_end=233
  _globals['_BYTETENSOR']._serialized_start=235
  _globals['_BYTETENSOR']._serialized_end=325
  _globals['_TENSORLIST']._serialized_start=327
  _globals['_TENSORLIST']._serialized_end=356
  _globals['_SERVERMODEL']._serialized_start=454
  _globals['_SERVERMODEL']._serialized_end=613
# @@protoc_insertion_point(module_scope)
