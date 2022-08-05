from descubreartistas.filter.functions import *
from descubreartistas.audiofeatures.analisis import calcula_media
import matplotlib.pyplot as plt


def compare_hist_feature(fichero, feature, columna_filtro, filtro, salida):
    """Función que muestra varios histogramas con la densidad de
    probabilidad de los valores de feature seleccionados, para todos los
    elementos de filtro que corresponden a la columna columna_filtro

    Argumentos:
        fichero: nombre del archivo a leer
        feature: valor a usar para el cálculo de la densidad de probabilidad
        columna_filtro: nombre de la columna que filtrará
        filtro: filtro que han de cumplir los elementos de columna_filtro
        salida: nombre del archivo a escribir

    Devuelve:
        datos_generados: devuelve los datos generados para construir la gráfica
        peso_generados: devuelve los pesos generados para construir la gráfica
    """
    datos_generados = []
    peso_generados = []
    fig = plt.figure()
    # Titulo para el gráfico
    titulo = ""
    # Se genera cada uno de los histogramas y se pintan
    for i in filtro:
        titulo += " - " + i
        datos, peso = hist_feature(fichero, feature, columna_filtro, i, False, False)
        plt.hist(datos, bins=50, alpha=0.5, weights=peso, label=i)
        datos_generados.append(datos)
        peso_generados.append(peso)
    plt.ylabel("Densidad de probabilidad")
    plt.title("Histograma de " + feature + " comparando" + titulo)
    plt.legend(loc="upper right")
    plt.show(block=False)
    fig.savefig(salida)
    return datos_generados, peso_generados


def hist_feature(fichero, feature, columna_filtro, filtro, salida, mostrar=True):
    """Función que muestra un histograma con la densidad de probabilidad de
    los valores de feature seleccionados, filtrados previamente
    por el valor de filtro en la columna columna_filtro

    Argumentos:
        fichero: nombre del archivo a leer
        feature: valores a usar para el cálculo de la densidad de probabilidad
        columna_filtro: nombre de la columna que filtrará
        filtro: filtro que han de cumplir los elementos de columna_filtro
        salida: nombre del archivo a escribir
        mostrar: indica si muestra y guarda la gráfica o no. True por defecto

    Devuelve:
        valores: valores calculados para el histograma
        weight: peso único repetido calculado para el histograma
    """
    # Se leen los datos
    valores = filtra_columna(fichero, feature, columna_filtro, filtro)
    # Se transforman a decimal y se ponen de manera uniforme
    valores = [round(float(i), 3) for i in valores]
    # Se calculan los pesos para la densidad
    weight = [1 / len(valores) for i in valores]
    if mostrar:
        fig = plt.figure()
        plt.hist(valores, bins=50, weights=weight)
        plt.ylabel("Densidad de probabilidad")
        plt.title("Histograma de " + feature + " de " + filtro[0])
        plt.show(block=False)
        fig.savefig(salida)
    return valores, weight


def grafico_media(fichero, feature, columna, columna_filtro, filtro, salida):
    """Función que muestra una gráfica con la media de los valores de feature
    agrupados para columna, filtrados previamente por el valor de filtro
    en la columna columna_filtro

    Argumentos:
        fichero: nombre del archivo a leer
        feature: valores a calcular la media
        columna: nombre de la columna para agrupar los elementos a mostrar
        columna_filtro: nombre de la columna que filtrará
        filtro: filtro que han de cumplir los elementos de columna_filtro

    Devuelve:
        media_feature: datos generados para el gráfico
    """
    # Se crea un diccionario para guardar los datos
    media_feature = dict()
    # Se filtran los datos para quedarse con los valores únicos que hay que representar
    datos = multiples_filtros(fichero, columna, columna_filtro, filtro, False)
    for elemento in datos:
        # Se extraen los valores del elemento para la feature bajo estudio
        valores = filtra_columna(fichero, feature, columna, [elemento])
        media_feature[elemento] = calcula_media([float(i) for i in valores])
    # Se pinta la gráfica, se le da formato y se guarda
    fig = plt.figure()
    plt.plot(
        media_feature.keys(),
        media_feature.values(),
        color="green",
        linestyle="dashed",
        linewidth=2,
        marker="o",
        markerfacecolor="blue",
        markersize=10,
    )
    plt.xticks(rotation="vertical")
    plt.xlabel(columna)
    plt.ylabel(feature)
    plt.title(feature + " VS " + columna + " para " + filtro[0])
    fig.tight_layout()
    plt.show(block=False)
    fig.savefig(salida)
    return media_feature
