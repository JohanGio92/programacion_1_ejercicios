import csv
def leer_camion(filename):
    truck = []
    with open(filename, "rt") as file:
        rows = csv.reader(file)
        next(rows)
        for row in rows:
            lote = (row[0], int(row[1]), float(row[2]))
            truck.append(lote)
    return truck

truck = leer_camion('../02_Estructuras_y_Funciones/camion.csv')
print(truck)
