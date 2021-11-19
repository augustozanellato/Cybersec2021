## Description
Using a debugging tool will be extremely useful on your missions. Can you run this program in gdb and find the flag?

## Solution
The solution is provided as a gdb script `solution.gdb` that can be executed with `gdb --batch --command=solution.gdb ./run`.
The program tells us that the flag is being read to the global variable `flag_buf` so we can just insert a breakpoint just before program exit and print it.
