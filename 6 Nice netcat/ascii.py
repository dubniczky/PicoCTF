import os

with open('data.txt', 'r', encoding='utf8') as f:
    data = f.readlines()
    
for line in data:
    line = line[:-2]
    print(chr(int(line)), end='')
print()