## Description
The program runs several checks to detect a debugging environment. If running into gdb, every test should FAIL.
Patch the program to obtain PASS in every check even when running into gdb
## Solution
A patch is provided in `patch.txt`.
It's not very hard to patch, we just need to patch each test function to return 0.
(Fun fact: one of the checks (`ldhook`) might be broken, on my machine it fails without any debugger attached)
