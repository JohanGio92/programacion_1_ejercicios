import csv

def parse_csv(nombre_archivo, select = None, types = None, has_headers = True):

    assert has_headers and select
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)

        # Lee los encabezados del archivo
        if has_headers:
            encabezados = next(filas)

        # Si se indicó un selector de columnas,
        #    buscar los índices de las columnas especificadas.
        # Y en ese caso achicar el conjunto de encabezados para diccionarios
        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []

        registros = []
        for fila in filas:
            if not fila:    # Saltear filas vacías
                continue

            # Filtrar la fila si se especificaron columnas
            if indices:
                fila = [fila[index] for index in indices]

            # Convierto la Fila al tipo especificado
            if types:
                fila = [type(value) for type, value in zip(types, fila[:len(types)])]

            # Armar el diccionario
            registro = dict(zip(encabezados, fila)) if has_headers else tuple(fila)
            registros.append(registro)

    return registros


camion = parse_csv("../data/camion.csv", select = ['nombre','precio'], has_headers=True)
print(camion)
