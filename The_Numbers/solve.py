alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

numbers = [ 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14 ]

print('picoCTF{', end='')
for i in numbers:
    print(alphabet[i-1], end='')
print('}')