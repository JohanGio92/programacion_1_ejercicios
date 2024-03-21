# hipoteca.py
MESES_DEL_ANIO = 12

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
PAGO_EXTRA = 1000
total_pagado = 0.0
cantidad_de_meses = 1

pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

def esta_entre_los_meses(mes):
    return pago_extra_mes_comienzo <= mes and mes <= pago_extra_mes_fin


while saldo > 0:
    if esta_entre_los_meses(cantidad_de_meses):
        saldo -= PAGO_EXTRA
        total_pagado += PAGO_EXTRA

    saldo = saldo * (1 + tasa / MESES_DEL_ANIO) - pago_mensual
    total_pagado = total_pagado + pago_mensual
    print(str(cantidad_de_meses) + ' ' + str(total_pagado) + ' ' + str(round(saldo, 2)))
    cantidad_de_meses += 1

print('Total pagado', round(total_pagado, 2))
print('meses ', cantidad_de_meses - 1)
