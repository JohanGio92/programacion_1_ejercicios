import csv
from collections import Counter
from pprint import pprint
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

def costo_camion(trucks):
    costo_camion = 0
    for truck in trucks:
        costo_camion += truck["precio"] * truck["cajones"]
    return costo_camion

def costo_precios(trucks, prices):
    costo_precios = 0
    for truck in trucks:
        for price in prices:
            if truck['nombre'] in price:
                costo_precios += price[truck['nombre']] * truck['cajones']

    return costo_precios;

def coste_total(truck, prices):
    return costo_precios(truck, prices) - costo_camion(truck)


def hacer_informe(trucks, prices):
    reports = []
    for truck in trucks:
        for price in prices:
            if truck['nombre'] in price:
                reports.append(tuple(truck.values()) + tuple(price.values()))
    return reports

trucks = leer_camion('../data/camion.csv')
prices = leer_precios('../data/precios.csv')

##pprint(trucks)
##pprint(prices)
pprint(hacer_informe(trucks, prices))
