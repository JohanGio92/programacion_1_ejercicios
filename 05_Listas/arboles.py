import csv
from pprint import pprint
def leer_parque(filename):

    with open(filename, 'rt', encoding="utf-8") as file:
        rows = csv.reader(file)
        headers = next(rows)
        parks = [ dict(zip(headers, row)) for row in rows ]

    return parks

trees = leer_parque('../data/arbolado-en-espacios-verdes.csv')
pprint(trees)
