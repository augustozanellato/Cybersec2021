import codecs

orig_data = codecs.encode("El Psy Congroo", "ascii")
enc_data = codecs.decode(b"IFhiPhZNYi0KWiUcCls=", "base64")
enc_flag = codecs.decode(b"I3gDKVh1Lh4EVyMDBFo=", "base64")


def xor(s1: bytes, s2: bytes) -> bytes:
    return bytes([b1 ^ b2 for (b1, b2) in zip(s1, s2)])


key = xor(orig_data, enc_data)
orig_flag = xor(enc_flag, key)
ascii_flag = codecs.decode(orig_flag, "ascii")
print(ascii_flag)
