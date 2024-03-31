# precondicion: acepta numero postivos y negativos
# postcondicion: devolver un numero positivo si es negativo o el mismo numero
def valor_absoluto(n):
    # n es un numero
    if n >= 0:
        return n
    else:
        return -n

# precodicion: lista diferente de none y la lista acepta numeros positivos y negativos
# postcondicion: devolver un numero entre 0 y suma de sus pares
# invariante: si el numero es par sumo sino sumo 0
def suma_pares(l):
    # res: result, e: aNumber, l: numberList
    res = 0
    for e in l:
        if e % 2 == 0:
            res += e
        else:
            res += 0

    return res

#precondicion: a acepta cualquier numero, b debe ser una numero mayor que 0
#poscondicion: devolver a * b
def veces(a, b):
    # res: result, a: aNumber, b: otherNumber, nb: times
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res

# precondiciones: n tiene que ser un numero positivo
# postcondicones: devolver un numero entre 1 en adelante
# invariante: si n es par n//2 sino al numero 3*n +1  hasta llegar al numero hasta 1
def collatz(n):
    # res: result, n: aNumber
    res = 1

    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1

    return res

