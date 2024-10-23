import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
	return enc

def b16_decode(enc):
	dec = ""
	for i in range(0, len(enc), 2):
		a = "{0:04b}".format( ALPHABET.find(enc[i]) )
		b = "{0:04b}".format( ALPHABET.find(enc[i+1]) )
		dec += chr(int(a + b, 2))
	return dec
		

def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]

def back_shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 - t2) % len(ALPHABET)]

cipher = "dcebcmebecamcmanaedbacdaanafagapdaaoabaaafdbapdpaaapadanandcafaadbdaapdpandcac"


for i in range(16):
	key = chr(LOWERCASE_OFFSET + i)
	dec = ""
	for i, c in enumerate(cipher):
		dec += back_shift(c, key[i % len(key)])
	print(b16_decode(dec))
	


# redacted, a -> hcgfgegbgdhegfge

