## Solution
After disassembling the program it looks like the input string gets compared byte by byte with (hex) `46 6c 34 67` which in ascii is `Fl4g`.
The flag can also be retrieved using `strings hello_world` which extracts human readable strings from executables

## Flag
```
Flage{reverse_hello_world}
```
