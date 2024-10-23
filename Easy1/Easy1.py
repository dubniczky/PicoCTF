alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

cipher = 'UFJKXQZQUNB'
key =    'SOLVECRYPTO'


result = ''
for i in range(len(key)):
    cNum = alphabet.index(cipher[i])
    kNum = alphabet.index(key[i])
    newNum = (cNum + kNum) % len(alphabet)
    result += alphabet[newNum]
    print(f'{cipher[i]} {key[i]}, {cNum} {kNum} -> {newNum} = {alphabet[newNum]}')

print('picoCTF{', result, '}', sep='')