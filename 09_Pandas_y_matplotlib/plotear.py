
import matplotlib.pyplot as plot
import numpy


def plotear_senos_y_cosenos():
    ejex = numpy.linspace(-numpy.pi, numpy.pi, 256)
    coseno_x = numpy.cos(ejex)
    seno_x = numpy.sin(ejex)
    figure, axes = plot.subplots()
    axes.plot(ejex, coseno_x)
    axes.plot(ejex, seno_x)
    plot.show()


if __name__ == '__main__':

    #plotear_senos_y_cosenos()

    plot.figure(figsize= (8, 6), dpi= 80)
    axe = plot.subplot(1, 1, 1)
    ejex = numpy.linspace(-numpy.pi, numpy.pi, 256)
    coseno_x = numpy.cos(ejex)
    seno_x = numpy.sin(ejex)

    axe.plot(ejex, coseno_x, color = "blue", linewidth = 2, linestyle = "--")
    axe.plot(ejex, seno_x, color = "red", linewidth = 2, linestyle = "--")
    axe.set_xlim(-4, 4)
    axe.set_ylim(-1.0, 1.0)
    axe.set_xticks(numpy.linspace(-4, 4, 9))
    axe.set_yticks(numpy.linspace(-1, 1, 5))
    plot.savefig('../data/senos_y_cosenos.png', dpi = 72)
    plot.show()
