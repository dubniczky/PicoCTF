with open('enc', 'r', encoding='utf8') as f:
    flag = f.read()
    
def encode(flag):
    return ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

def encode_reveng(flag):
    return ''.join(
        [ 
            chr(   (ord(flag[i]) << 8)  +  ord(flag[i + 1]) )
            for i in range(0, len(flag), 2)
        ]
    )
    
def decode(flag):
    return ''.join([chr(ord(flag[i]) >> 8) + chr(ord(flag[i]) & 0xff) for i in range(len(flag))])


print(decode(flag))
