import csv

def parse_csv(nombre_archivo, select = None, types = None, has_headers = True, silence_errors = False):

    assert has_headers
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

        i = 0

        for fila in filas:
            i += 1
            if not fila:    # Saltear filas vacías
                continue

            # Filtrar la fila si se especificaron columnas
            if indices:
                fila = [fila[index] for index in indices]

            # Convierto la Fila al tipo especificado
            if types:
                try:
                    fila = [type(value) for type, value in zip(types, fila[:len(types)])]
                except ValueError:
                    if not silence_errors:
                        print(f'Fila {i}: No puede convertir {fila}')
                        print(f'Fila {i}: Motivo: invalid literal for int() with base 10: \'\'')

            # Armar el diccionario
            registro = dict(zip(encabezados, fila)) if has_headers else tuple(fila)
            registros.append(registro)

    return registros


camion = parse_csv('../data/missing.csv', types = [str, int, float], silence_errors=True)
print(camion)
