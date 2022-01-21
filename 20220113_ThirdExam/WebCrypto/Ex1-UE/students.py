# read the secret
with open("secret.txt", "r") as file:
    challenge = file.read()
    file.close()

for _ in range(15):
    challenge = challenge.decode("base64")
print(challenge)
