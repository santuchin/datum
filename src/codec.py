from __future__ import annotations
import builtins
import typing

from . import base, rows

class Codec:

    def __init__(self, encode, decode, /) -> None:

        self.encode = encode
        self.decode = decode

    @builtins.staticmethod
    def from_class(cls: builtins.type, /) -> Codec:
        return Codec(cls.encode, cls.decode)

raw = Codec(
    lambda obj: obj,
    lambda idx: idx
)

bytes = Codec(
    lambda obj: base.decode_bytes(obj),
    lambda idx: base.encode_bytes(idx)
)

int = Codec(
    lambda obj: (obj * 2 - 1) if (0 < obj) else -(obj * 2),
    lambda idx: -(idx // 2) if (0 == idx % 2) else (idx // 2 + 1)
)

bool = Codec(
    lambda obj: 1 if obj else 0,
    lambda idx: True if idx else False
)

memoryview = Codec(
    lambda obj: bytes.encode(builtins.bytes(obj)),
    lambda idx: builtins.memoryview(bytes.decode(idx))
)

bytearray = Codec(
    lambda obj: bytes.encode(builtins.bytes(obj)),
    lambda idx: bytearray(bytes.decode(idx))
)

complex = Codec(
    lambda obj: rows.encode([float.encode(obj.real), float.encode(obj.imag)]),
    lambda idx: complex(*map(float.decode, rows.decode(idx, 2)))
)

range = Codec(
    lambda obj: rows.encode([int.encode(obj.start), int.encode(obj.stop), int.encode(obj.step)]),
    lambda idx: range(*map(int.decode, rows.decode(idx, 3)))
)

def str(encoding: builtins.str='utf-8', errors='strict') -> Codec:

    return Codec(
        lambda obj: bytes.encode(obj.encode(encoding, errors)),
        lambda idx: bytes.decode(idx).decode(encoding, errors)
    )

def eval(globals: typing.Dict[builtins.str, typing.Any]={}, locals: typing.Dict[builtins.str, typing.Any]={}) -> Codec:

    codec = str()

    return Codec(
        lambda obj: codec.encode(builtins.repr(obj)),
        lambda idx: builtins.eval(codec.decode(idx), globals, locals)
    )

def option(*options: builtins.tuple[typing.Any]) -> Codec:

    return Codec(
        lambda obj: options.index(obj),
        lambda idx: options[idx]
    )

def fraction(denominator: builtins.int, /) -> Codec:

    return Codec(
        lambda obj: int.encode(builtins.int(obj * denominator)),
        lambda idx: int.decode(idx) / denominator
    )

def charmap(symbols: builtins.str, /) -> Codec:

    return Codec(
        lambda obj: base.decode(obj, symbols),
        lambda idx: base.encode(idx, symbols)
    )

def add(codec: Codec, extra: builtins.tuple[typing.Any]) -> Codec:

    length = len(extra)

    return Codec(
        lambda obj: (extra.index(obj)) if (obj in extra) else (length - 1 + codec.encode(obj)),
        lambda idx: (extra[idx]) if (length > idx) else (codec.decode(length - 1 + idx))
    )

def combine(codecs: typing.Dict[type, Codec]) -> Codec:

    length = len(codecs)

    keys = tuple(codecs)
    values = tuple(codecs.values())

    print(keys, values)

    return Codec(
        lambda obj: codecs[type(obj)].encode(obj) * length + keys.index(type(obj)),
        lambda idx: values[idx % length].decode(idx // length)
    )

defaults = {
    builtins.bytes: bytes,
    builtins.int: int,
    builtins.bool: bool,
    builtins.str: str(),
    builtins.memoryview: memoryview,
    builtins.bytearray: bytearray,
    builtins.complex: complex,
    builtins.range: range,
    builtins.float: fraction(100),

    None: raw,
    builtins.eval: eval(),
}
