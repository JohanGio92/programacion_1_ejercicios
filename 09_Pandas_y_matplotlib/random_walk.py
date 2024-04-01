import numpy
import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos = np.random.randint (-1,2,largo)
    total_de_pasos =  pasos.cumsum()
    return total_de_pasos

if __name__ == '__main__':

    trayectorias = 12
    N = 100000

    figure = plt.figure()
    axe = plt.subplot(2, 1, 1)

    maximo = -numpy.inf
    minimo = numpy.inf
    distancia_mas_alejada = None
    distancia_menos_alejada = None

    for i in range(trayectorias):
        caminata = randomwalk(N)
        axe.plot(caminata)

        distancia_mas_alejada = numpy.abs(caminata).max()
        if distancia_mas_alejada > maximo:
            maximo = distancia_mas_alejada
            caminata_mas_alejada = caminata

        distancia_menos_alejada = numpy.abs(caminata).min()
        if minimo > distancia_menos_alejada:
            minimo = distancia_menos_alejada
            caminata_menos_alejada = caminata


    axe = plt.subplot(2, 2, 3)
    axe.plot(caminata_mas_alejada)
    axe = plt.subplot(2, 2, 4)
    axe.plot(caminata_menos_alejada)

    axe.set_xlabel("Tiempo")
    axe.set_ylabel("Distancia al Origen")
    plt.show()
