import fileparse
def leer_camion(filename):
    return fileparse.parse_csv(filename, types=[str, int, float])

def leer_precios(filename):
    prices = fileparse.parse_csv(filename, types=[str, float], has_headers =False)
    return [{price[0]: price[1]} for price in prices]
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

def imprimir_informe(reports):
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    print('%10s %10s %10s %10s' % headers)
    print('---------- ---------- ---------- ----------')
    for nombre, cajones, precio, cambio in reports:
        precio = '$%.2f' % precio
        print('%10s %10d %10s %10.2f' % (nombre, cajones, precio, cambio))

def informe_camion(camion_filename='../data/camion.csv', precios_filename='../data/precios.csv'):
    trucks = leer_camion(camion_filename)
    prices = leer_precios(precios_filename)
    reports = hacer_informe(trucks, prices)
    imprimir_informe(reports)

def f_principal(parameters):
    if len(parameters) != 3:
        raise SystemExit(f'el nombre del archivo: {parameters[0]} necesita 2 parametros de nombre de arhivo cvs')
    informe_camion(parameters[1], parameters[2])

if __name__ == '__main__':
    import sys
    f_principal(sys.argv)
