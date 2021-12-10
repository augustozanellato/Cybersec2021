## Description
This is a position-independent binary which gives you a module address, and a trivial write-what-where.
Can you spawn a shell?
## Solution
This challenge is very similar to the previous but this time we have a PIE executable so we don't know where the GOT will be when the program is loaded in memory.
Luckily the program leaks the address of the start of the `main` function, using that we can calculate the random offset at which the executable is loaded and thus obtain the addresses of the GOT and of out target function.
We can then use those addresses to pwn the binary in the same way as the previous challenge.
