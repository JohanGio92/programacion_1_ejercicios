
def imprimir_tabla_de_multiplicar():

    tabla_del_nueve = 9

    print('    ', end = '')
    for i in range(tabla_del_nueve + 1):
        print(f'{i:>3d}', end=' ')
    print('\n--------------------------------------------')

    for i in range(tabla_del_nueve + 1):
        print(f'{i:>2d}:', end=' ')
        for j in range(tabla_del_nueve + 1):
            print(f'{i*j:>3d}', end=' ')
        print()

imprimir_tabla_de_multiplicar()
