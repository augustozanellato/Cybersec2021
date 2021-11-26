# handly-shellcode - 50pt

### Challenge ###
> This program executes any shellcode that you give it. Can you spawn a shell and use that to read the flag.txt? You can find the program in /problems/handy-shellcode_4_037bd47611d842b565cfa1f378bfd8d9 on the shell server.


### Hints ###
> You might be able to find some good shellcode online.

### Solution ###

We have a program that asks us an shellcode.

If we provide to it an working shellcode, it will perform this shellcode.

### Executing the exploit ###

We can get an working shellcode in http://shell-storm.org/shellcode/.

You can use exploit.py that cointains an shellcode and sends it to the programm

## Solution
There really wasn't a thinking process involved with the solution of this one, pwntools gives us a ready made shellcode for popping a shell using `shellcraft`
