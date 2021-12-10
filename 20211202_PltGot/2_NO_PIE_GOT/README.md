## Description
if you mess some bytes around, you might print the flag :)
## Solution
This challenge is the same as the previous, we have another trivial write-what-where, using that we can overwrite one of the GOT entries in order to get the program to call the function that we want, in this case `win`
