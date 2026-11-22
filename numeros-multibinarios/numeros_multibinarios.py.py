def converteBase(n, base):
    if n == 0:
        return [0]
    algarismos = []
    while n > 0:
        algarismos = [n %  base] + algarismos
        n = n // base
    return algarismos

def procuraZeroUm(l):
    if len(l) == 0:
        return True
    if l[0] != 0 and l[0] != 1:
        return False
    return procuraZeroUm(l[1:])

def multibinario(n):
    for base in range(2, 6):
        if not procuraZeroUm(converteBase(n, base)):
            return False
    return True

#BP
intervalo = int(input("Procurar multibinários até: "))
multiB = []
for n in range(2, intervalo + 1):
    if multibinario(n):
        multiB.append(n)
print("Números multibinários (bases 2 a 5):", multiB)