from pwn import *  # type: ignore

context.binary = "./CrossTheBridge_patched"
p = process()
p.sendline(b"y")
p.sendline()
p.send(b"L\n" * 16)
log.success(p.recvline_regex(rb".*{.*}.*").decode("ascii"))
