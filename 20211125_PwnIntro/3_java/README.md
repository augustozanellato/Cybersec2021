## Description
Comparing strings in assembly is an hard task for java n00bs.

## Solution
By looking at the source we can see that there's a struct containing a string followed by a function pointer, if we can somehow overflow the string buffer we can jump to an arbitrary location.
One interesting destination might be the last line of the `bash` function which happens to have an offset of `0x32` from the start of the function.
The user input handling doesn't check string bounds so we can easily overflow the buffer and pop a shell.
## Flag
`flag{this_is_a_flag}`
