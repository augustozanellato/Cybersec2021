from codecs import decode

key = "".join(format(ord(x), "b").rjust(8, "0") for x in "Mu")
R = 2
expected_ciphertext = "01100101" "00100010" "10001100" "01011000" "00010001" "10000101"


def halfblock_expand(b: str) -> str:
    return b[0] + b[1] + b[3] + b[2] + b[3] + b[2] + b[4] + b[5]


def key_expand(key: str, index: int) -> str:
    index = index % len(key)
    expkey = key[index : index + 8]
    if (keylen := len(expkey)) < 8:
        expkey += key[: 8 - keylen]
    return expkey


def xor(a: str, b: str) -> str:
    assert len(a) == len(b)
    res = ""
    for i in range(len(a)):
        res += "1" if a[i] != b[i] else "0"
    return res


def S1(b: str) -> str:
    # fmt: off
    s = [
        "101", "010", "001", "110", "011", "100", "111", "000",
        "001", "100", "110", "010", "000", "111", "101", "011",
    ]
    # fmt: on
    return s[int(b, 2)]


def S2(b: str) -> str:
    # fmt: off
    s = [
        "100", "000", "110", "101", "111", "001", "011", "010",
        "101", "011", "000", "111", "110", "010", "001", "100",
    ]
    # fmt: on
    return s[int(b, 2)]


def block_count(text: str) -> int:
    return int(len(text) // 12)


def get_block(text: str, idx: int) -> str:
    return text[idx * 12 : (idx + 1) * 12]


def split_at(s: str, split_idx: int) -> tuple[str, str]:
    return s[:split_idx], s[split_idx:]


def encrypt_block(block: str, i: int) -> str:
    for r in range(R):  # Rule 4
        Lr, Rr = split_at(block, 6)  # Rule 5
        rule6 = halfblock_expand(Rr)
        rule7 = xor(rule6, key_expand(key, i * R + r))
        s1, s2 = split_at(rule7, 4)
        r9L = S1(s1)
        r9R = S2(s2)
        r10 = r9L + r9R
        r11 = xor(r10, Lr)
        block = Rr + r11
    return block


def encrypt(plaintext: str) -> str:
    ciphertext = ""
    assert len(plaintext) % 12 == 0  # Rule 1
    assert len(key) >= 8  # Rule 2
    for i in range(block_count(plaintext)):  # Rule 3
        ciphertext += encrypt_block(get_block(plaintext, i), i)
    return ciphertext


blocks = block_count(expected_ciphertext)
cracked_plaintext = ""
for block in range(blocks):
    block_ciphertext = get_block(expected_ciphertext, block)
    print(f"Cracking block#{block} {block_ciphertext}... ", end="")
    for current_plaintext in range(2 ** 12):
        current_plaintext = format(current_plaintext, "b").rjust(12, "0")
        ciphertext = encrypt_block(current_plaintext, block)
        if ciphertext == block_ciphertext:
            print(f"CRACKED: {current_plaintext}")
            cracked_plaintext += current_plaintext
            break
    else:
        print("FAILED :(")
print(f"Cracked plaintext: {cracked_plaintext}")
readable_plaintext = decode(int(cracked_plaintext, 2).to_bytes(len(cracked_plaintext) // 8, "big"), "ascii")
print(f'ASCII plaintext: "{readable_plaintext}"')
