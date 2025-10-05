from . import codec, base

class Value:

	def __init__(self, path: str, codec_: codec.Codec=None, /) -> None:

		if codec_ in codec.defaults:
			self.codec = codec.defaults[codec_]

		else:
			self.codec = codec_

		try:
			file = open(path, 'rb')
			self.value = self.codec.decode(base.decode_bytes(file.read()))
			file.close()
	
		except FileNotFoundError:
			self.value = self.codec.decode(0)

		self.path = path

	def save(self, /) -> None:

		file = open(self.path, 'wb')
		file.write(base.encode_bytes(self.codec.encode(self.value)))
		file.close()
