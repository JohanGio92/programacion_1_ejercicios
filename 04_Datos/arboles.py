import csv
from pprint import pprint
def leer_parque(filename, parkname):

    with open(filename, 'rt', encoding="utf-8") as file:
        rows = csv.reader(file)
        headers = next(rows)
        parks = []
        for row in rows:
            if parkname in row:
                parks.append(dict(zip(headers, row)))

    return parks

pprint(leer_parque('../data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ'))
