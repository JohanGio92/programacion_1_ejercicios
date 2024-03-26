
import numpy
def buscar_u_elemento(list, data):
    try:
        list.reverse()
        return len(list) - list.index(data) - 1
    except ValueError:
        return -1

def maximo(lista):

    maxValue = -numpy.Infinity

    for value in lista:
        if value > maxValue:
            maxValue = value

    return maxValue

def invertir_lista(list):
    inverted_list = []
    for data in list:
        inverted_list.insert(0, data)
    return inverted_list


print(buscar_u_elemento([1,2,3,2,3,4],1))
print(buscar_u_elemento([1,2,3,2,3,4],2))
print(buscar_u_elemento([1,2,3,2,3,4],3))
print(buscar_u_elemento([1,2,3,2,3,4],5))

print(maximo([1,2,7,2,3,4]))
print(maximo([1,2,3,4]))
print(maximo([-5,4]))
print(maximo([-5,-4]))
print(maximo([-25,-45, -15]))

print(invertir_lista([1, 2, 3, 4, 5]))
print(invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']))
