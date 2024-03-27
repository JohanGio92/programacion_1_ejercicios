import random
import numpy

CANTIDAD_DE_DADOS = 5
INTENTOS = 3
NUMEROS_DE_CARAS = 6
def tirar():
    return [random.randint(1,NUMEROS_DE_CARAS) for i in range(CANTIDAD_DE_DADOS)]

def es_generala(dados):
    return len(set(dados)) == 1

def prob_generala(REPETICIONES):
    generalas = []

    for i in range(REPETICIONES):
        ok = False
        for i in range(INTENTOS):
            ok = es_generala(tirar())
            if ok: break
        generalas.append(ok)

    cantidad_de_servidas = sum(generalas)
    return cantidad_de_servidas / REPETICIONES



REPETICIONES = 100000

cantidad_de_servidas = sum([es_generala(tirar()) for i in range(REPETICIONES)])
probabilidad = cantidad_de_servidas/REPETICIONES
print(f'Tiré {REPETICIONES} veces, de las cuales {cantidad_de_servidas} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {probabilidad:.6f}.')

print(f'El probabilidad es: {prob_generala(REPETICIONES)}')
