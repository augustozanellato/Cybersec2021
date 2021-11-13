with open("ciphertext.txt", "r") as ciphertext_file:
    ciphertext = ciphertext_file.read().lower()

trans = str.maketrans(
    "abcdefghijklmnopqrstuvwxyz",
    "IMZOPKSTEBWGNRVL_UJAYHF_DC",
)

print(ciphertext.translate(trans))
