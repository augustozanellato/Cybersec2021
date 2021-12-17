# CrossTheBridge

## Description

Can you cross the bridge and get the flag?

You must not patch the "play_game_no_patch" function, nor delete it, and this function must be executed to get the flag.
The rest of the binary can be patched in any way you like!

## Solution

See the attached `patch.diff` file. A pwntools script (`solution.py`) is also provided, it just sends the required output and prints the flag, nothing interesting to see there.
There's a function that checks if the user has cheated using a `ptrace()` check, it's easily patched by changing a conditional jump to an unconditional one (`JZ`=>`JMP`)
The other patch consists in making the `generate_random_step()` function always return `'L'` so that the bridge isn't random anymore.

## Flag

```plain
SPRITZ{WhaT_A_fUn_gAme}
```
