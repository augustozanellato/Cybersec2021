## Solution
We have to overflow the buffer named `buffer` and overwrite `main()` return address to point to the `shell()` function entry point in order to pop a shell.
`gets()` is used for the input. `gets` doesn't check the buffer bounds so exploitation is ez.

## Flag
`encryptCTF{Buff3R_0v3rfl0W5_4r3_345Y}`
