import string
from random import choices

alphabet = string.ascii_letters + string.digits

print("".join(choices(alphabet, k=10)))
