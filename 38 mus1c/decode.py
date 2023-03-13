# Read
with open('output.txt', 'r') as f:
    lines = f.read().splitlines()
    
# Convert
nums = [int(l) for l in lines]
chars = [chr(n) for n in nums]

# Create flag
print('picoCTF{', end='')
print(''.join(chars), end='')
print('}')