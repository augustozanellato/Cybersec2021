## Description
I made a simple shell which allows me to run some specific commands on my server can you test it for bugs?

## Solution
This one is a little bit trickier: to pass the challenge we need to know the x86 stack layout.
The idea is overflowing the buffer `buffer`, overwriting `main()` return address to be `lol()` function entrypoint.
We'll also need to provide shellcode where `lol` stack base will be.

## Flag
`encryptCTF{N!c3_j0b_jump3R}`
