## Description
Open and read the flag!
## Solution
Both a patch and a gdb script are included here (it can be done without the gdb script but I was too lazy to patch out the `remove` call).
The patch just skips the piece of code that overwrites the flag with `*`, the gdb script breaks the program execution just before `remove` so the file isn't yet deleted and the it prints out the flag.
## Flag
`SharifCTF{b70c59275fcfa8aebf2d5911223c6589}`
