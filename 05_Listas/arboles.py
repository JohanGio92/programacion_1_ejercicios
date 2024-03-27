import csv
from pprint import pprint
def leer_parque(filename):

    with open(filename, 'rt', encoding="utf-8") as file:
        rows = csv.reader(file)
        headers = next(rows)
        parks = [ dict(zip(headers, row)) for row in rows ]

    return parks

def alturas_del_arboles(trees, speciesName):
    return [float(tree['altura_tot']) for tree in trees if speciesName == tree['nombre_com']]

def alturas_por_diametro_de_los_arboles(trees, speciesName):
    return [ tuple( [float(tree['altura_tot']), float(tree['diametro']) ]) for tree in trees if speciesName == tree['nombre_com']]

trees = leer_parque('../data/arbolado-en-espacios-verdes.csv')
# pprint(trees)
#pprint(alturas_del_arboles(trees, speciesName='Jacarandá'))
pprint(alturas_por_diametro_de_los_arboles(trees, speciesName='Jacarandá'))
