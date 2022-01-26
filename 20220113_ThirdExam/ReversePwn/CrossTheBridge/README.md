# CrossTheBridge

## Description

Can you find a way to cross the random bridge and get the flag every time you want?

The bridge generation MUST REMAIN randomic at every run. You MUST provide a solution able to work in such a case, i.e., you must describe a way to retrieve the correct path and win legally every time you play.
You MUST NOT patch the "play_game_no_patch" function and all the functions called inside, nor delete them.
"play_game_no_patch" must be executed to get the flag.
Solutions directly jumping to "print_flag" or similar WILL NOT BE CONSIDERED. If you feel your solution is somewhat breaking these rules, please ask the teacher.
The rest of the binary can be patched in any way you like!

## Solution

The base idea is patching out the debugger check and the printing out the generated brige using gdb and then using it to win the game.
**Full solution coming soon**
