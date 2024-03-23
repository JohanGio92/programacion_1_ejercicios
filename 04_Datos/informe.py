import csv, pprint

def leer_camion(filename):
    truck = []
    total_cost = 0
    with open(filename, "rt") as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            try:
                truck.append(dict(zip(headers, row)))
            except ValueError:
                raise "Value incorrect"
    return truck

def costo_camion(trucks):
    total = lambda trucks: (
        sum(int(truck["cajones"]) * float(truck["precio"]) for truck in trucks)
    )
    return total(trucks)

if __name__ == "__main__":
    trucks = leer_camion('../data/camion.csv')
    pprint.pprint(trucks)
    pprint.pprint(f'costo del camion:  {costo_camion(trucks)}')
