import sys


FILENAME = "../data/camion.csv"
QUANTITY_PARAMETERS = len(sys.argv)
MAX_PARAMETERS = 2

def costo_camion(filename):
    cost = 0
    with open(filename, "rt", encoding="utf-8") as camion_file:
        next(camion_file)

        for row in camion_file:
            name, crate, price = row.split(',')
            cost += float(crate) * float(price)
    return cost

if __name__ == "__main__":
    cost = 0
    if QUANTITY_PARAMETERS == MAX_PARAMETERS:
        cost = costo_camion(sys.argv[MAX_PARAMETERS])
    else:
        cost = costo_camion(FILENAME)
    print("Costo total {}".format(cost))
