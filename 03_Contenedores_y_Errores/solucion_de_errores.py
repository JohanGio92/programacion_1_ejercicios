import pprint

#%
#Ejercicio 3.5. Función tiene_a()
#Comentario: El error era de tipo semantico.
#El error radicaba en que no hacia toda la iteracion en la cadena, y a la primera iterecion retornaba true o false
#    Lo corregí cambiando 2 return por 1 (codigo limpio).
#    Lo corregí cambiando a la primera ocurrencia encontrada 'a' returna a True.
#    A continuación va el código corregido
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    ok = False
    while i < n and not ok:
        if expresion[i] == 'a':
            ok = True
        i += 1
    return ok

print(tiene_a('UNSAM 2020'))
print(tiene_a('abracadabra'))
print(tiene_a('La novela 1984 de George Orwell'))

#%
#Ejercicio 3.6. Función tiene_a()
#Comentario: El error era de tipo sintactico.
# El error radicaba en la sentencias 'while' y 'if' le falta agregar los ':'
# cambie la comparacion dentro del 'if' de '=' por '=='
# cambie el return de 'Falso' por 'False'
#    A continuación va el código corregido
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')

#%
#Ejercicio 3.7. Función tiene_uno()
#Comentario: El error en tiempo de ejecucion.
#El error radicaba en que la funcion 'tiene_uno' esta pensado para pasarle como parametro un cadena
# y al mandarle un parametro de tipo integer te arroja una excepcion de tipo TypeError, con el siguiente mensaje:
# TypeError: object of type 'int' has no len()
#    Lo corregí cambiando el parametro pasado 1984 (int) a '1984' (string)
def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno('1984')

#%
#Ejercicio 3.8. Función suma()
# Error: Semantico
# Solucion: agregando un return de 'c'
def suma(a,b):
    c = a + b
    return c

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

import csv
from pprint import pprint

#%
#Ejercicio 3.8. Función leer_camion()
# Error: Semantico
# comentarios sobre el error: El error radica en que la variable camion es una lista de diccionarios
# donde cada indice de la lista tiene la misma direccion de memoria
# Solucion: crear nuevas direcciones de memoria para la creacion del diccionario
def leer_camion(nombre_archivo):
    camion=[]
    registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            camion.append({
                encabezado[0]:fila[0],
                encabezado[1]:fila[1],
                encabezado[2]: fila[2]
            })
    return camion

camion = leer_camion('../data/camion.csv')
pprint(camion)

