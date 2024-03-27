
import numpy
import random
import time

random.seed(time.time())
def crear_album(figus_total):
    return numpy.zeros(figus_total)

def album_incompleto(figuritas):
    return 0 in figuritas

def comprar_figu(figus_total):
    return random.randint(0, figus_total - 1)

def cuantas_figus(figus_total):
    album = crear_album(figus_total)

    while album_incompleto(album):
        figura_comprada = comprar_figu(figus_total)
        album[figura_comprada] += 1

    cantidad_de_figuras = numpy.sum(album)
    return cantidad_de_figuras


def experimento_figus(n_repeticiones, figus_total):
    return numpy.mean([ cuantas_figus(figus_total) for _ in range(n_repeticiones) ])


n_repeticiones = 100
figus_total = 670
print(experimento_figus(n_repeticiones, figus_total))
