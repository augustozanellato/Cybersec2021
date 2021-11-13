import random
import string


def transformation(input):
    input = list(input)
    input.append(input[0])
    input.pop(0)
    return "".join(input)


def reverse_transformation(input):
    input = list(input)
    input.insert(0, input[-1])
    input.pop()
    return "".join(input)


def encrypt(input, seed):
    input = transformation(input)
    input = list(input)
    random.seed(seed)
    input = [chr(ord(x) ^ random.randint(80, 120)) for x in input]
    input = "".join(input)
    return input


def decrypt(input, seed):
    random.seed(seed)
    return reverse_transformation("".join(chr(ord(char) ^ random.randint(80, 120)) for char in input))


with open("./secret.txt", "r") as file:
    cipher = file.read()

out = dict()
for seed in range(1000):
    decrypted = decrypt(cipher, seed)
    if set(decrypted).issubset(set(string.ascii_letters + string.digits + "}{_")) and "spritz" in decrypted:
        print(decrypted)
        out[seed] = decrypted
