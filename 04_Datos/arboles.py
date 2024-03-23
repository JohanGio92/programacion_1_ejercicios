import csv
from pprint import pprint
from collections import Counter
import statistics
def leer_parque(filename, parkname):

    with open(filename, 'rt', encoding="utf-8") as file:
        rows = csv.reader(file)
        headers = next(rows)
        parks = []
        for row in rows:
            if parkname in row:
                parks.append(dict(zip(headers, row)))

    return parks

def especies(trees):
    return set([tree['nombre_com'] for tree in trees])

def contar_ejemplares(trees):
    treeCount = Counter()

    for tree in trees:
        treeCount[tree['nombre_com']] += 1
    return treeCount

def obtener_alturas(trees, specieName):
    return [ float(tree['altura_tot']) for tree in trees if tree['nombre_com'] == specieName ]

trees = leer_parque('../data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')
#pprint(trees)
#pprint(especies(trees))
#pprint(contar_ejemplares(trees).most_common(5))
pprint(max(obtener_alturas(trees, 'Jacarandá')))
pprint(statistics.mean(obtener_alturas(trees, 'Jacarandá')))
