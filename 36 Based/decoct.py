target = "154 151 147 150 164"
target = target.split(" ")

octs = [int(i, 8) for i in target]
letters = [chr(i) for i in octs]

print(''.join(letters))