import string

expected_freqs = {
    "a": 8.4966,
    "b": 2.0720,
    "c": 4.5388,
    "d": 3.3844,
    "e": 11.1607,
    "f": 1.8121,
    "g": 2.4705,
    "h": 3.0034,
    "i": 7.5448,
    "j": 0.1965,
    "k": 0.2902,
    "l": 5.4893,
    "m": 3.0129,
    "n": 6.6544,
    "o": 7.1635,
    "p": 3.1671,
    "q": 0.1962,
    "r": 7.5809,
    "s": 5.7351,
    "t": 6.9509,
    "u": 3.6308,
    "v": 1.0074,
    "w": 1.2899,
    "x": 0.2902,
    "y": 1.7779,
    "z": 0.2722,
}


def calculate_frequencies(text: str) -> dict[str, float]:
    letter_count = dict()
    count = 0
    for character in text:
        if character not in string.ascii_lowercase:
            continue
        letter_count[character] = letter_count.get(character, 0) + 1
        count += 1
    return {k: v / count * 100 for k, v in letter_count.items()}


with open("ciphertext.txt", "r") as ciphertext_file:
    ciphertext = ciphertext_file.read().lower()

actual_freqs = calculate_frequencies(ciphertext)
print(actual_freqs)
key: dict[str, str] = dict()
for actual_freq in actual_freqs.items():
    error = 100
    min_err_value = ("", 0)
    for expected_freq in expected_freqs.items():
        current_error = abs(actual_freq[1] - expected_freq[1])
        if current_error < error:
            error = current_error
            min_err_value = expected_freq
    key[actual_freq[0]] = min_err_value[0]
    expected_freqs.pop(min_err_value[0])
print(key)
plaintext = "".join(char if char not in string.ascii_lowercase else key[char] for char in ciphertext)
print(plaintext)
