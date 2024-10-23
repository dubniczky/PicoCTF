import string

alphabet = 'abcdefghijklmnopqrstuvwxyz'
offset = -7
cipher = 'wpjvJAM{jhlzhy_k3jy9wa3k_lh60l00i}'

def dec_char(character, offset):
    ind = alphabet.find(character.lower())
    if ind == -1:
        return character
    return alphabet[ (ind + offset) % len(alphabet) ]

res = ""
for c in cipher:
    res += dec_char(c, offset)

print(res)