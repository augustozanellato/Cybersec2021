import string
from random import choices
alphabet = string.ascii_letters + string.digits + string.punctuation

print("".join(choices(alphabet, k=int(input("Inserisci una lunghezza: ")))))