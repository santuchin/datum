
BYTES = bytes(range(2**8))
NONZERO = bytes(range(1, 2**8))

def encode(number: int, symbols: bytes) -> bytearray:

	base = len(symbols)
	result = bytearray()

	while number:
		number, rem = divmod(number - 1, base)
		result.append(symbols[rem])

	return result

def encode_bytes(number: int) -> bytearray:

	result = bytearray()

	while number:
		number, rem = divmod(number - 1, 256)
		result.append(rem)

	return result

def encode_nonzero(number: int) -> bytearray:

	result = bytearray()

	while number:
		number, rem = divmod(number - 1, 255)
		result.append(rem + 1)

	return result

def decode(number, symbols) -> int:

	base = len(symbols)
	result = 0

	for digit in reversed(number):
		result = result * base + 1 + symbols.index(digit)

	return result

def decode_bytes(number) -> int:

	result = 0

	for digit in reversed(number):
		result = (result << 8) + 1 + digit
	
	return result

def decode_nonzero(number) -> int:

	result = 0

	for digit in reversed(number):
		result = (result << 8) - result + digit
		# this is the same as:
		# result = (result * 255) - 1 + digit

	return result
