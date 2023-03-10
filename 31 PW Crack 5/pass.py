import hashlib

with open('dictionary.txt', 'r') as f:
    passlist = f.read().splitlines()

def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()

for pw in passlist:
    print(pw, hash_pw(pw).hex())