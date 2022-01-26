# GameOfThrones

## Description

Can you write a decent finale for Game of Thrones and get the flag?

You cannot patch this binary.
The challenge MUST BE SOLVED by providing appropriate inputs.
Solutions that jump directly to the print flag function WILL NOT BE CONSIDERED.
Do not modify the flag.txt file.

## Solution

See `solution.py`.
The binary provides a trivial write-what-where so it would be a good idea to overwrite some entry in the GOT in order to get control of the program control flow.
A good candidate for the overwrite would be (as usual) the `exit()` function.
The function that gives us the flag is `show_true_ending()` but it's never called anywhere.
By overwriting the GOT entry for `exit()` we can call the required function and get the flag.

## Flag

```plain
SPRITZ{GoT_Hijacking_iS_FUn{flag}}
```
