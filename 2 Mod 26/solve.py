# Rot 13
alphabet = "abcdefghijklmnopqrstuvwxyz"
Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

c = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_hyLicInt}"

offset = 13
for i, _ in enumerate(c):
    if c[i] in alphabet:
        print(alphabet[(alphabet.index(c[i]) + offset) % 26], end='')
    elif c[i] in Alphabet:
        print(Alphabet[(Alphabet.index(c[i]) + offset) % 26], end='')
    else:
        print(c[i], end='')
print()