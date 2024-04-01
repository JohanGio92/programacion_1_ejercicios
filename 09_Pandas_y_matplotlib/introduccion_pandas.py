
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def caminata_al_azar():
    idx = pd.date_range('20200923 14:00', periods=120, freq='min')
    s1 = pd.Series(np.random.randint(-1, 2, 120), index=idx)
    s2 = s1.cumsum()
    s2.plot()
    w = 5  # ancho en minutos de la ventana
    s3 = s2.rolling(w).mean()
    s3.plot()
    df_series_23 = pd.DataFrame([s2, s3]).T  # armo un dataframe con ambas series
    print(df_series_23)
    df_series_23.plot()
    plt.show()

def doce_personas_caminando_doce_horas():
    horas = 8
    idx = pd.date_range('20200923 14:00', periods=horas * 60, freq='min')
    nombres = ['Pedro', 'Santiago', 'Juan', 'Andrés', 'Bartolomé', 'Tiago', 'Isca', 'Tadeo', 'Mateo', 'Felipe', 'Simón', 'Tomás']

    df_walks = pd.DataFrame(np.random.randint(-1, 2, [horas * 60, 12]).cumsum(axis=0), index=idx, columns=nombres)
    print(df_walks)
    df_walks.plot()

    w = 45
    df_walk_suav = df_walks.rolling(w, min_periods=1).mean()  # datos suavizados
    nsuav = ['S_' + n for n in nombres]
    df_walk_suav.columns = nsuav  # cambio el nombre de las columnas
    # para los datos suavizados
    df_walk_suav.plot()
    plt.show()


def boxplot(arbolado):
    df_lineal_seleccion = filter_arbolado(arbolado)
    df_lineal_seleccion.boxplot("diametro_altura_pecho", by='nombre_cientifico')
    plt.show()


def filter_arbolado(arbolado):
    cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']
    especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']
    df_lineal = arbolado[cols_sel]
    df_lineal_seleccion = df_lineal[df_lineal["nombre_cientifico"].isin(especies_seleccionadas)]
    return df_lineal_seleccion

def pairplot(arbolado):
    df_lineal_seleccion = filter_arbolado(arbolado)
    sns.pairplot(df_lineal_seleccion, hue = "nombre_cientifico")
    plt.show()


if __name__ == '__main__':

    #caminata_al_azar()
    #doce_personas_caminando_doce_horas()
    arbolado = pd.read_csv('../data/arbolado-publico-lineal-2017-2018.csv')
    #boxplot(arbolado)
    pairplot(arbolado)


