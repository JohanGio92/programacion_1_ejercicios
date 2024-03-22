import csv
def leer_camion(filename):
    truck = []
    with open(filename, "rt") as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            try:
                lote = {headers[0]: row[0], headers[1]: int(row[1]), headers[2]: float(row[2])}
                truck.append(lote)
            except ValueError:
                raise "Value incorrect"
    return truck

truck = leer_camion('../data/camion.csv')
print(truck)
