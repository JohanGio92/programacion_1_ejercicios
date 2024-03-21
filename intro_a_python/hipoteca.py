# hipoteca.py
MESES_DEL_ANIO = 12

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
PAGO_EXTRA = 1000
total_pagado = 0.0
cantidad_de_meses = 0


while saldo > 0:
    if cantidad_de_meses < MESES_DEL_ANIO:
        saldo -= PAGO_EXTRA
        total_pagado += PAGO_EXTRA

    saldo = saldo * (1 + tasa / MESES_DEL_ANIO) - pago_mensual
    total_pagado = total_pagado + pago_mensual
    cantidad_de_meses += 1

print('Total pagado', round(total_pagado, 2))
print('meses ', cantidad_de_meses)
