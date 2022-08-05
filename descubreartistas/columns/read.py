import pandas as pd
from functools import reduce


def get_column_pandas(input_file, column_name):
    """Función que para un archivo dado y una columna devuelve una lista
    con los elementos de la columna a partir de un método de pandas

    Argumentos:
        input_file: nombre del archivo a leer
        column_name: nombre de la columna a leer

    Devuelve:
        list(): lista con los valores de la columna
    """
    # Se retorna la columna seleccionada, asegurando que es una lista de los elementos
    # y no una lista de listas
    return reduce(
        lambda x, y: x + y,
        pd.read_csv(input_file, sep=";", usecols=[column_name]).values.tolist(),
    )


def get_column_lines(input_file, column_name):
    """Función que para un archivo dado y una columna devuelve una lista
    con los elementos de la columna procesando línea a línea el fichero

    Argumentos:
        input_file: nombre del archivo a leer
        column_name: nombre de la columna a leer

    Devuelve:
        elementos: lista con los valores de la columna
    """
    # Se genera la lista para contener la columna
    elementos = list()

    # Se abre el fichero para leerlo
    with open(input_file, "r") as f:
        # Se lee una línea para extraer la cabecera
        cabecera = f.readline().split(sep=";")
        # Se busca que columna es la que se quiere mostrar
        ind = -1
        for col in cabecera:
            if col == column_name:
                ind = cabecera.index(col)

        if ind != -1:
            # Se recorre linea a linea el fichero
            for line in f:
                # Se busca la columna con el estado
                elementos.append(line.split(sep=";")[ind])
    return elementos
