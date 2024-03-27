import csv
from pprint import pprint
def leer_parque(filename):

    with open(filename, 'rt', encoding="utf-8") as file:
        rows = csv.reader(file)
        headers = next(rows)
        parks = [ dict(zip(headers, row)) for row in rows ]

    return parks

def alturas_del_arboles(trees, specieName):
    return [float(tree['altura_tot']) for tree in trees if specieName == tree['nombre_com']]

def alturas_por_diametro_de_los_arboles(trees, specieName):
    return [( float(tree['altura_tot']), float(tree['diametro']) ) for tree in trees if specieName == tree['nombre_com']]

def medidas_de_especies(trees, speciesName):
    return  { tree['nombre_com']: (float(tree['altura_tot']), float(tree['diametro'])) for tree in trees if tree['nombre_com'] in speciesName }

trees = leer_parque('../data/arbolado-en-espacios-verdes.csv')
# pprint(trees)
# pprint(sum(alturas_del_arboles(trees, specieName='Jacarandá')))
#pprint(alturas_por_diametro_de_los_arboles(trees, specieName='Jacarandá'))
#pprint(alturas_por_diametro_de_los_arboles(trees, specieName='Eucalipto'))
#pprint(alturas_por_diametro_de_los_arboles(trees, specieName='Palo borracho rosado'))
#pprint(medidas_de_especies(trees, ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']))
