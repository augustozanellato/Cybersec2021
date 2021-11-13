# First challenge

## Description

A begger gave us an envelop with two letters:

- ciphertext.txt
- compass.png

He told us that he use to sing this song during CTF exercises.
Can you help us decrypt the song?

Note: the final plaintext must have only "lowercase" letters

Rules:

- You cannot use online tools to solve the challenge automatically.
- Provide a Python solution, where you explain every consolidation you made to achieve the solution.

Some useful python commands:

```py
#read the ciphertext text
with open("ciphertext.txt", "r") as file:
    cipher = ''.join(file.readlines())
```

## Writeup

Looks like we need to write an auto solver for a substitution cipher.
The idea behind it is determining the frequency of each letter in the ciphertext and substituting it with the letter that has the nearest frequency in the given table.

## Aftertoughts (=> things I wish I figured out during the exam)

The provided frequencies are too different from the actual frequencies encountered in the text so it's not trivial to algorithmically crack the cipher.
Luckily it's not hard to manually crack it because we know the flag format so we know that `nvdeak` maps to `spritz`, exploiting that we can manually crack a letter at a time (see `manual.py`)

## Flag

`SPRITZ{OASIS_ENCRYPT}
