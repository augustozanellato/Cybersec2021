# NeedsToBeHappy

## Description

Can you make the man happy and get the flag?

You cannot patch this binary. The challenge must be solved by providing appropriate inputs.
Do not modify the temp file.

## Solution

See `solution.py`.
The binary provides a trivial write-what-where so it would be a good idea to overwrite some entry in the GOT in order to get control of the program control flow.
A good candidate for the overwrite would be (as usual) the `exit()` function.
The function that (sort of) gives us the flag is `give_the_man_a_cat()` but it's never called anywhere.
By overwriting the GOT entry for `exit()` we can call the required function and get the flag.

## Flag

```plain
SPRITZ{PaRiPpaPPaA}
```
