
import matplotlib.pyplot as plot
import numpy
def plotear_temperaturas():
    temperaturas = numpy.load('../data/temperaturas.npy')
    plot.hist(temperaturas, bins = 30)
    plot.show()

plotear_temperaturas()
