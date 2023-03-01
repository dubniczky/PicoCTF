from binascii import unhexlify

def rev(h):
    return unhexlify(h)[::-1]

flag = b"".join(
    [
        rev("6f636970"),
        rev("7b465443"),
        rev("306c5f49"),
        rev("345f7435"),
        rev("6d5f6c6c"),
        rev("306d5f79"),
        rev("5f79336e"),
        rev("35386130"),
        rev("32356533"),
    ]
).decode()

print(flag)

# 0x8657350__0x804b000__0x80489c3__0xf7f12d80__0xffffffff__0x1__0x8655160__0xf7f20110__0xf7f12dc7__(nil)__0x8656180__0x1__0x8657330__0x8657350__0x6f636970__0x7b465443__0x306c5f49__0x345f7435__0x6d5f6c6c__0x306d5f79__0x5f79336e__0x35386130__0x32356533__0xff89007d__0xf7f4daf8__0xf7f20440__0x110a8d00__0x1