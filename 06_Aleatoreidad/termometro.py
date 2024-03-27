import random
import statistics
def medir_temp(repeticiones):
    temperatura_real = 37.5
    return [temperatura_real + random.normalvariate(mu = 0, sigma = 0.2) for _ in range(repeticiones)]

def resumen_temp(repeticiones):
    mediciones = medir_temp(repeticiones)
    maximo = max(mediciones)
    minimo = min(mediciones)
    promedio = sum(mediciones) / repeticiones
    mediana = statistics.median(mediciones)
    return maximo, minimo, promedio, mediana

repeticiones = 1000
maximo, minimo, promedio, mediana = resumen_temp(repeticiones)

print(f"Máximo: {maximo:.2f}")
print(f"Mínimo: {minimo:.2f}")
print(f"Promedio: {promedio:.2f}")
print(f"Mediana: {mediana:.2f}")
