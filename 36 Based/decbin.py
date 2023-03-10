target = "01100001 01101110 01101001 01101101 01100001 01110100 01101001 01101111 01101110"
target = target.replace(" ", "")

def decode_binary_string(s):
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))

print(decode_binary_string(target))