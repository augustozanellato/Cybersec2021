## Description
can you spawn a shell and get the flag?
## Solution
We have a trivial write-what-where, using that we can overwrite one of the GOT entries in order to get the program to call the function that we want, in this case `win`
