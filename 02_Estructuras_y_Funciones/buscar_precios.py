
def buscar_precios(searchedfruit):
    file = open('precios.csv', 'rt')
    ok = False

    for line in file:
        *fruit, price = line.split(',')
        if searchedfruit in fruit:
            ok = True
            break

    if ok:
        print(f'El precio de un cajon de {searchedfruit} es {price}')
    else:
        print(f'{searchedfruit} no figura en la lista de precios')


buscar_precios('Frambuesa')
buscar_precios('Kale')
