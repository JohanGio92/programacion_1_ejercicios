import random
import numpy

def tirar():
    return [ random.randint(1,6) for i in range(5) ]

def es_generala(dados):
    return len(set(dados)) == 1

N = 100000

G = sum([es_generala(tirar()) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')
