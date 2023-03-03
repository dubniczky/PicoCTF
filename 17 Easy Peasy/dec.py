p1s = '5541103a246e415e036c4c5f0e3d415a513e4a560050644859536b4f57003d4c'
p2s = '6227295e455c7838375c7866375c7862355c786430635c7838665c7863365c78'

# bytes from hex string
p1b = bytes.fromhex(p1s)
p2b = bytes.fromhex(p2s)

def enc(a, b):
    res = bytes()
    for i in range(len(b)):
        res += bytes([a[i] ^ b[i]])
    return res

p2enc = enc(p1b, p2b)

for b in p2enc:
    print(chr(b), end='')
print()

