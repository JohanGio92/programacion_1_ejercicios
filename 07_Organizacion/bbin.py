def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos

def donde_insertar(lista, x, verbose=False):
    '''Usa Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve 0 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    Si no se encuentra x, devuelve la posición donde debería insertarse en la lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            return medio  # elemento encontrado
        elif lista[medio] < x:
            izq = medio + 1  # descarto mitad izquierda
        else:
            der = medio - 1  # descarto mitad derecha
    return izq

def insertar(lista, x):

    posicion = busqueda_binaria(lista, x)

    if busqueda_binaria(lista, x) == -1:
        posicion = donde_insertar(lista, x)
        lista.insert(posicion, x)

    return posicion

