## Description
I'll let you in on a secret; a useful string "/bin/cat flag.txt" is present in this binary, as is a call to system(). It's just a case of finding them and chaining them together to make the magic happen.

## Solution
Luckily pwntools does all the hard work for us, we just need to overflow the stack up to the point where the `pwnme` return address is stored.
The binary provides everything that's needed to pwn this one so we just need to call `system` with the address of the `usefulString` as an argument.
