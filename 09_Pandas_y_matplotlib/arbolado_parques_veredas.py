import matplotlib.pyplot as plt
import pandas as pd

def make_dataframe(filename, filter_columns, added_column, isRename = True):
    dataframe = pd.read_csv(filename)
    dataframe_filtered = dataframe[filter_columns].copy()

    if isRename:
        renamed = dict(zip(filter_columns, ['altura_arbol', 'diametro_altura_pecho', 'nombre_cientifico']))
        dataframe_filtered = dataframe_filtered.rename(columns= renamed)

    dataframe_filtered[[added_column[0]]] = added_column[1]

    return dataframe_filtered

def  make_boxplot(dataframe, column):
    dataframe.boxplot(column = column, by = 'ambiente')
    plt.title("Arbolado En Parques")
    plt.ylabel(column.capitalize().replace("_", " "))
    plt.show()



if __name__ == '__main__':

    df_tipas_parques = make_dataframe(
        filename = "../data/arbolado-en-espacios-verdes.csv",
        filter_columns = ['altura_tot', 'diametro', 'nombre_cie'],
        added_column=("ambiente", "parque"),
    )

    df_tipas_veredas = make_dataframe(
        filename = "../data/arbolado-publico-lineal-2017-2018.csv",
        filter_columns = ['altura_arbol', 'diametro_altura_pecho', 'nombre_cientifico'],
        added_column=("ambiente", "vereda"),
        isRename = False
    )

    df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])
    make_boxplot(dataframe = df_tipas, column = "diametro_altura_pecho")
    make_boxplot(dataframe = df_tipas, column = "altura_arbol")


