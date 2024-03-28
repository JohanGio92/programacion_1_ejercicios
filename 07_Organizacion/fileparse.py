import csv

def parse_csv(nombre_archivo, types = None, has_headers = True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)

        # Lee los encabezados del archivo
        if has_headers:
            encabezados = next(filas)

        registros = []
        for fila in filas:
            if not fila:    # Saltear filas vacías
                continue
            # Convierto laFila al tipo especificado
            if types:
                fila = [type(value) for type, value in zip(types, fila[:len(types)])]

            # Armar el diccionario
            registro = dict(zip(encabezados, fila)) if has_headers else tuple(fila)
            registros.append(registro)

    return registros

camion = parse_csv('../data/precios.csv', [str, float], has_headers = False)
print(camion)
