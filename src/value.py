from . import codec, base

class Value:

	def __init__(self, path: str, codec: codec.Codec=None, /) -> None:

		if codec in codec.defaults:
			self.codec = codec.defaults[codec]

		else:
			self.codec = codec

		try:
			file = open(path, 'rb')
			self.obj = self.codec.decode(base.decode_bytes(file.read()))
			file.close()
	
		except FileNotFoundError:
			self.obj = self.codec.decode(0)

		self.path = path

	def save(self, /) -> None:

		file = open(self.path, 'wb')
		file.write(base.encode_bytes(self.codec.encode(self.obj)))
		file.close()
