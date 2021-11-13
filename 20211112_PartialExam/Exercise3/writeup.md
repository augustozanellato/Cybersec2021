# Third challenge

## Description

SPRITZ group deployed a new encryption strategy ... but they forgot to write
the decryption part.

Can you help them?

The main.py contains the encryption code they used, and an encrypted secret contained
contained in secret.txt .

Be careful: the encryption function require, an information we do not have.
We only now that it is an integer greater than 0, and for sure lower than 1000.

## Rules

- Provide us a python solution to decrypt the "secret.txt".
- You cannot use online tools to solve the exercise automatically.

## Writeup

The provided transformation is just taking the first letter of the string and moving it to the last place so it's easy to reverse.
The encryption is just XORing characters with a random int generated from the seed.
So we'll need to bruteforce the seed somehow
We should be able to recognize the flag due to the known format (and the guessable character set `A-Za-z0-9{}_`)

## Flag

`spritz{final_chall}`
