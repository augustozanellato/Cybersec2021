import requests

alphabet = "abcdef1234567890"

for letter in alphabet:
    r = requests.get(f"http://localhost:124/?pass={letter}", headers={"User-Agent": letter})
    response = r.text
    lines = [line for line in response.splitlines() if line and "<" not in line]
    if lines:
        print(f"found flag: {lines[0]}")
