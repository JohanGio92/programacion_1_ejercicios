import informe_final
def leer_camion(filename):
    return informe_final.leer_camion(filename)

def costo_camion(trucks):
    total = lambda trucks: (
        sum(int(truck["cajones"]) * float(truck["precio"]) for truck in trucks)
    )
    return total(trucks)

def f_principal(parameters):
    if len(parameters) != 2:
        raise SystemExit(f'el nombre del archivo: {parameters[0]} necesita 1 parametros de nombre de arhivo camion.cvs')

    trucks = leer_camion(parameters[1])
    print(f'costo total:  {costo_camion(trucks)}')

if __name__ == '__main__':
    import sys
    f_principal(sys.argv)
