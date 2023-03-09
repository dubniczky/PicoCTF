python -c "print(chr(0x33) + chr(0x39) + chr(0x63) + chr(0x65))" | \
    python level2.py | \
    grep "picoCTF"