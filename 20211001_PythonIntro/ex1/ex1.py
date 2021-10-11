orig = input("Inserisci una stringa: ")

letters_base = ord("a")
letters_count = ord("z") - letters_base + 1

print("".join([chr(letters_base + ((ord(ch) - letters_base + 2) % letters_count)) for ch in orig]))
