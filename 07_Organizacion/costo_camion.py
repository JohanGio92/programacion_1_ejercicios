import csv, pprint
import informe_funciones

def leer_camion(filename):
    return informe_funciones.leer_camion(filename)

def costo_camion(trucks):
    total = lambda trucks: (
        sum(int(truck["cajones"]) * float(truck["precio"]) for truck in trucks)
    )
    return total(trucks)

#trucks = leer_camion('../data/camion.csv')
#pprint.pprint(trucks)
#pprint.pprint(f'costo del camion:  {costo_camion(trucks)}')
