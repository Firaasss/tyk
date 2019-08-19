# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: coprocess_session_state.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='coprocess_session_state.proto',
  package='coprocess',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1d\x63oprocess_session_state.proto\x12\tcoprocess\"*\n\nAccessSpec\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x0f\n\x07methods\x18\x02 \x03(\t\"s\n\x10\x41\x63\x63\x65ssDefinition\x12\x10\n\x08\x61pi_name\x18\x01 \x01(\t\x12\x0e\n\x06\x61pi_id\x18\x02 \x01(\t\x12\x10\n\x08versions\x18\x03 \x03(\t\x12+\n\x0c\x61llowed_urls\x18\x04 \x03(\x0b\x32\x15.coprocess.AccessSpec\"/\n\rBasicAuthData\x12\x10\n\x08password\x18\x01 \x01(\t\x12\x0c\n\x04hash\x18\x02 \x01(\t\"\x19\n\x07JWTData\x12\x0e\n\x06secret\x18\x01 \x01(\t\"!\n\x07Monitor\x12\x16\n\x0etrigger_limits\x18\x01 \x03(\x01\"\xfd\x07\n\x0cSessionState\x12\x12\n\nlast_check\x18\x01 \x01(\x03\x12\x11\n\tallowance\x18\x02 \x01(\x01\x12\x0c\n\x04rate\x18\x03 \x01(\x01\x12\x0b\n\x03per\x18\x04 \x01(\x01\x12\x0f\n\x07\x65xpires\x18\x05 \x01(\x03\x12\x11\n\tquota_max\x18\x06 \x01(\x03\x12\x14\n\x0cquota_renews\x18\x07 \x01(\x03\x12\x17\n\x0fquota_remaining\x18\x08 \x01(\x03\x12\x1a\n\x12quota_renewal_rate\x18\t \x01(\x03\x12@\n\raccess_rights\x18\n \x03(\x0b\x32).coprocess.SessionState.AccessRightsEntry\x12\x0e\n\x06org_id\x18\x0b \x01(\t\x12\x17\n\x0foauth_client_id\x18\x0c \x01(\t\x12:\n\noauth_keys\x18\r \x03(\x0b\x32&.coprocess.SessionState.OauthKeysEntry\x12\x31\n\x0f\x62\x61sic_auth_data\x18\x0e \x01(\x0b\x32\x18.coprocess.BasicAuthData\x12$\n\x08jwt_data\x18\x0f \x01(\x0b\x32\x12.coprocess.JWTData\x12\x14\n\x0chmac_enabled\x18\x10 \x01(\x08\x12\x13\n\x0bhmac_secret\x18\x11 \x01(\t\x12\x13\n\x0bis_inactive\x18\x12 \x01(\x08\x12\x17\n\x0f\x61pply_policy_id\x18\x13 \x01(\t\x12\x14\n\x0c\x64\x61ta_expires\x18\x14 \x01(\x03\x12#\n\x07monitor\x18\x15 \x01(\x0b\x32\x12.coprocess.Monitor\x12!\n\x19\x65nable_detailed_recording\x18\x16 \x01(\x08\x12\x37\n\x08metadata\x18\x17 \x03(\x0b\x32%.coprocess.SessionState.MetadataEntry\x12\x0c\n\x04tags\x18\x18 \x03(\t\x12\r\n\x05\x61lias\x18\x19 \x01(\t\x12\x14\n\x0clast_updated\x18\x1a \x01(\t\x12\x1d\n\x15id_extractor_deadline\x18\x1b \x01(\x03\x12\x18\n\x10session_lifetime\x18\x1c \x01(\x03\x12\x16\n\x0e\x61pply_policies\x18\x1d \x03(\t\x12\x13\n\x0b\x63\x65rtificate\x18\x1e \x01(\t\x1aP\n\x11\x41\x63\x63\x65ssRightsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12*\n\x05value\x18\x02 \x01(\x0b\x32\x1b.coprocess.AccessDefinition:\x02\x38\x01\x1a\x30\n\x0eOauthKeysEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x62\x06proto3')
)




_ACCESSSPEC = _descriptor.Descriptor(
  name='AccessSpec',
  full_name='coprocess.AccessSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='coprocess.AccessSpec.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='methods', full_name='coprocess.AccessSpec.methods', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=44,
  serialized_end=86,
)


_ACCESSDEFINITION = _descriptor.Descriptor(
  name='AccessDefinition',
  full_name='coprocess.AccessDefinition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='api_name', full_name='coprocess.AccessDefinition.api_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='api_id', full_name='coprocess.AccessDefinition.api_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='versions', full_name='coprocess.AccessDefinition.versions', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='allowed_urls', full_name='coprocess.AccessDefinition.allowed_urls', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=88,
  serialized_end=203,
)


_BASICAUTHDATA = _descriptor.Descriptor(
  name='BasicAuthData',
  full_name='coprocess.BasicAuthData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='password', full_name='coprocess.BasicAuthData.password', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hash', full_name='coprocess.BasicAuthData.hash', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=205,
  serialized_end=252,
)


_JWTDATA = _descriptor.Descriptor(
  name='JWTData',
  full_name='coprocess.JWTData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='secret', full_name='coprocess.JWTData.secret', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=254,
  serialized_end=279,
)


_MONITOR = _descriptor.Descriptor(
  name='Monitor',
  full_name='coprocess.Monitor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trigger_limits', full_name='coprocess.Monitor.trigger_limits', index=0,
      number=1, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=281,
  serialized_end=314,
)


_SESSIONSTATE_ACCESSRIGHTSENTRY = _descriptor.Descriptor(
  name='AccessRightsEntry',
  full_name='coprocess.SessionState.AccessRightsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='coprocess.SessionState.AccessRightsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='coprocess.SessionState.AccessRightsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1159,
  serialized_end=1239,
)

_SESSIONSTATE_OAUTHKEYSENTRY = _descriptor.Descriptor(
  name='OauthKeysEntry',
  full_name='coprocess.SessionState.OauthKeysEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='coprocess.SessionState.OauthKeysEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='coprocess.SessionState.OauthKeysEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1241,
  serialized_end=1289,
)

_SESSIONSTATE_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='coprocess.SessionState.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='coprocess.SessionState.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='coprocess.SessionState.MetadataEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1291,
  serialized_end=1338,
)

_SESSIONSTATE = _descriptor.Descriptor(
  name='SessionState',
  full_name='coprocess.SessionState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='last_check', full_name='coprocess.SessionState.last_check', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='allowance', full_name='coprocess.SessionState.allowance', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rate', full_name='coprocess.SessionState.rate', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='per', full_name='coprocess.SessionState.per', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expires', full_name='coprocess.SessionState.expires', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quota_max', full_name='coprocess.SessionState.quota_max', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quota_renews', full_name='coprocess.SessionState.quota_renews', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quota_remaining', full_name='coprocess.SessionState.quota_remaining', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quota_renewal_rate', full_name='coprocess.SessionState.quota_renewal_rate', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='access_rights', full_name='coprocess.SessionState.access_rights', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='org_id', full_name='coprocess.SessionState.org_id', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='oauth_client_id', full_name='coprocess.SessionState.oauth_client_id', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='oauth_keys', full_name='coprocess.SessionState.oauth_keys', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='basic_auth_data', full_name='coprocess.SessionState.basic_auth_data', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='jwt_data', full_name='coprocess.SessionState.jwt_data', index=14,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hmac_enabled', full_name='coprocess.SessionState.hmac_enabled', index=15,
      number=16, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hmac_secret', full_name='coprocess.SessionState.hmac_secret', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_inactive', full_name='coprocess.SessionState.is_inactive', index=17,
      number=18, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='apply_policy_id', full_name='coprocess.SessionState.apply_policy_id', index=18,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_expires', full_name='coprocess.SessionState.data_expires', index=19,
      number=20, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='monitor', full_name='coprocess.SessionState.monitor', index=20,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable_detailed_recording', full_name='coprocess.SessionState.enable_detailed_recording', index=21,
      number=22, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='coprocess.SessionState.metadata', index=22,
      number=23, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='coprocess.SessionState.tags', index=23,
      number=24, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alias', full_name='coprocess.SessionState.alias', index=24,
      number=25, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_updated', full_name='coprocess.SessionState.last_updated', index=25,
      number=26, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id_extractor_deadline', full_name='coprocess.SessionState.id_extractor_deadline', index=26,
      number=27, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='session_lifetime', full_name='coprocess.SessionState.session_lifetime', index=27,
      number=28, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='apply_policies', full_name='coprocess.SessionState.apply_policies', index=28,
      number=29, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='certificate', full_name='coprocess.SessionState.certificate', index=29,
      number=30, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SESSIONSTATE_ACCESSRIGHTSENTRY, _SESSIONSTATE_OAUTHKEYSENTRY, _SESSIONSTATE_METADATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=317,
  serialized_end=1338,
)

_ACCESSDEFINITION.fields_by_name['allowed_urls'].message_type = _ACCESSSPEC
_SESSIONSTATE_ACCESSRIGHTSENTRY.fields_by_name['value'].message_type = _ACCESSDEFINITION
_SESSIONSTATE_ACCESSRIGHTSENTRY.containing_type = _SESSIONSTATE
_SESSIONSTATE_OAUTHKEYSENTRY.containing_type = _SESSIONSTATE
_SESSIONSTATE_METADATAENTRY.containing_type = _SESSIONSTATE
_SESSIONSTATE.fields_by_name['access_rights'].message_type = _SESSIONSTATE_ACCESSRIGHTSENTRY
_SESSIONSTATE.fields_by_name['oauth_keys'].message_type = _SESSIONSTATE_OAUTHKEYSENTRY
_SESSIONSTATE.fields_by_name['basic_auth_data'].message_type = _BASICAUTHDATA
_SESSIONSTATE.fields_by_name['jwt_data'].message_type = _JWTDATA
_SESSIONSTATE.fields_by_name['monitor'].message_type = _MONITOR
_SESSIONSTATE.fields_by_name['metadata'].message_type = _SESSIONSTATE_METADATAENTRY
DESCRIPTOR.message_types_by_name['AccessSpec'] = _ACCESSSPEC
DESCRIPTOR.message_types_by_name['AccessDefinition'] = _ACCESSDEFINITION
DESCRIPTOR.message_types_by_name['BasicAuthData'] = _BASICAUTHDATA
DESCRIPTOR.message_types_by_name['JWTData'] = _JWTDATA
DESCRIPTOR.message_types_by_name['Monitor'] = _MONITOR
DESCRIPTOR.message_types_by_name['SessionState'] = _SESSIONSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AccessSpec = _reflection.GeneratedProtocolMessageType('AccessSpec', (_message.Message,), dict(
  DESCRIPTOR = _ACCESSSPEC,
  __module__ = 'coprocess_session_state_pb2'
  # @@protoc_insertion_point(class_scope:coprocess.AccessSpec)
  ))
_sym_db.RegisterMessage(AccessSpec)

AccessDefinition = _reflection.GeneratedProtocolMessageType('AccessDefinition', (_message.Message,), dict(
  DESCRIPTOR = _ACCESSDEFINITION,
  __module__ = 'coprocess_session_state_pb2'
  # @@protoc_insertion_point(class_scope:coprocess.AccessDefinition)
  ))
_sym_db.RegisterMessage(AccessDefinition)

BasicAuthData = _reflection.GeneratedProtocolMessageType('BasicAuthData', (_message.Message,), dict(
  DESCRIPTOR = _BASICAUTHDATA,
  __module__ = 'coprocess_session_state_pb2'
  # @@protoc_insertion_point(class_scope:coprocess.BasicAuthData)
  ))
_sym_db.RegisterMessage(BasicAuthData)

JWTData = _reflection.GeneratedProtocolMessageType('JWTData', (_message.Message,), dict(
  DESCRIPTOR = _JWTDATA,
  __module__ = 'coprocess_session_state_pb2'
  # @@protoc_insertion_point(class_scope:coprocess.JWTData)
  ))
_sym_db.RegisterMessage(JWTData)

Monitor = _reflection.GeneratedProtocolMessageType('Monitor', (_message.Message,), dict(
  DESCRIPTOR = _MONITOR,
  __module__ = 'coprocess_session_state_pb2'
  # @@protoc_insertion_point(class_scope:coprocess.Monitor)
  ))
_sym_db.RegisterMessage(Monitor)

SessionState = _reflection.GeneratedProtocolMessageType('SessionState', (_message.Message,), dict(

  AccessRightsEntry = _reflection.GeneratedProtocolMessageType('AccessRightsEntry', (_message.Message,), dict(
    DESCRIPTOR = _SESSIONSTATE_ACCESSRIGHTSENTRY,
    __module__ = 'coprocess_session_state_pb2'
    # @@protoc_insertion_point(class_scope:coprocess.SessionState.AccessRightsEntry)
    ))
  ,

  OauthKeysEntry = _reflection.GeneratedProtocolMessageType('OauthKeysEntry', (_message.Message,), dict(
    DESCRIPTOR = _SESSIONSTATE_OAUTHKEYSENTRY,
    __module__ = 'coprocess_session_state_pb2'
    # @@protoc_insertion_point(class_scope:coprocess.SessionState.OauthKeysEntry)
    ))
  ,

  MetadataEntry = _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), dict(
    DESCRIPTOR = _SESSIONSTATE_METADATAENTRY,
    __module__ = 'coprocess_session_state_pb2'
    # @@protoc_insertion_point(class_scope:coprocess.SessionState.MetadataEntry)
    ))
  ,
  DESCRIPTOR = _SESSIONSTATE,
  __module__ = 'coprocess_session_state_pb2'
  # @@protoc_insertion_point(class_scope:coprocess.SessionState)
  ))
_sym_db.RegisterMessage(SessionState)
_sym_db.RegisterMessage(SessionState.AccessRightsEntry)
_sym_db.RegisterMessage(SessionState.OauthKeysEntry)
_sym_db.RegisterMessage(SessionState.MetadataEntry)


_SESSIONSTATE_ACCESSRIGHTSENTRY._options = None
_SESSIONSTATE_OAUTHKEYSENTRY._options = None
_SESSIONSTATE_METADATAENTRY._options = None
# @@protoc_insertion_point(module_scope)
