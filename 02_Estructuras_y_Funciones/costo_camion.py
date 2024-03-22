FILENAME = "../data/camion.csv"

def costo_camion(filename):
    cost = 0
    with open(filename, "rt", encoding="utf-8") as camion_file:
        next(camion_file)

        for row in camion_file:
            name, crate, price = row.split(',')
            cost += float(crate) * float(price)
    return cost

cost = costo_camion(FILENAME)

print("Costo total {}".format(cost))
