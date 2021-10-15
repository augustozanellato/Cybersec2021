import codecs
import random

with open("top_secret", "rb") as enc_file:
    enc_bytes = enc_file.read()

split_idx = 0
while (enc_bytes[-split_idx] ^ 0x88) != ord("."):
    split_idx += 1
split_idx += 10
message = enc_bytes[:-split_idx]
random_seed = bytes([b ^ 0x88 for b in enc_bytes[-split_idx:]])

print(f"Found random seed: {random_seed}")
random.seed(random_seed)
key = [random.randrange(256) for _ in message]
plaintext = [m ^ k for (m, k) in zip(message, key)]
print(codecs.decode(bytes(plaintext), "ASCII"))
