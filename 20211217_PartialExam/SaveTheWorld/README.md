# SaveTheWorld

## Description

We need your help to save the world. The selected fighter is too weak, do you have something to say about it?

You cannot patch this binary. Do not modify auxil1 and auxil2

## Solution

We have a trivial buffer overflow vulnerability, we just need to overwrite some stack variables with the correct values.
The input length isn't checked due to the use of `gets()` for handling user input, the target buffer is 72 bytes long, its content aren't checked against anything so we can just fill it with `A`s.
The only important thing here is overwriting the variables with the correct value and in the correct order (that's easily checked by looking at the variables position in the stack).

## Flag

```plain
SPRITZ{Yare_Yare}
```
