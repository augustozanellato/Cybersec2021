from operator import add, sub, mul, itruediv

ops = [add, sub, mul, itruediv]

a = float(input("Inserisci un numero: "))
b = float(input("Inserisci un altro numero: "))
op = int(input("Inserisci un operatore (0 per addizione, 1 per sottrazione, 2 per moltiplicazione oppure 3 per divisione: "))
print(ops[op](a, b))