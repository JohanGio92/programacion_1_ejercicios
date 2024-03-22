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

def leer_precios(filename):
    prices = []
    with open(filename, "rt") as file:
        rows = csv.reader(file)
        for row in rows:
            try:
                prices.append({row[0]: float(row[1])})
            except ValueError:
                raise "Value incorrect"
            except IndexError:
                break

    return prices

truck = leer_camion('../data/camion.csv')
print(truck)
prices = leer_precios('../data/precios.csv')
print(prices)
