from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class urmom(_message.Message):
    __slots__ = ("numberOfServers", "ip")
    NUMBEROFSERVERS_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    numberOfServers: int
    ip: str
    def __init__(self, numberOfServers: _Optional[int] = ..., ip: _Optional[str] = ...) -> None: ...

class Null(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
