from descubreartistas.filter.functions import filtra_columna
from math import sqrt


def similitud_euclidiana(datos_a, datos_b):
    """Función que calcula la similitud euclidiana para
     dos vectores dados

    Argumentos:
        datos_a: lista con los datos de un vector
        datos_b: lista con los datos del otro vector

    Devuelve:
        resultado: valor de similitud de los vectores
    """
    total = 0
    suma = sum(datos_a)
    for ind, i in enumerate(datos_a):
        datos_a[ind] = i / suma
    suma = sum(datos_b)
    for ind, i in enumerate(datos_b):
        datos_b[ind] = i / suma

    for ind, dato in enumerate(datos_a):
        total += (dato - datos_b[ind]) ** 2
    return 1 / (1 + sqrt(total))


def similitud_cosinus(datos_a, datos_b):
    """Función que calcula la similitud coseno para
     dos vectores dados

    Argumentos:
        datos_a: lista con los datos de un vector
        datos_b: lista con los datos del otro vector

    Devuelve:
        resultado: valor de similitud de los vectores
    """
    suma = sum(datos_a)
    for ind, i in enumerate(datos_a):
        datos_a[ind] = i / suma
    suma = sum(datos_b)
    for ind, i in enumerate(datos_b):
        datos_b[ind] = i / suma

    total_num = 0
    total_a = 0
    total_b = 0
    for ind, dato in enumerate(datos_a):
        total_num += dato * datos_b[ind]
        total_a += dato ** 2
        total_b += (datos_b[ind]) ** 2
    return total_num / (sqrt(total_a) * sqrt(total_b))


def densidad_probabilidad(datos):
    """Función que calcula la densidad de probabilidad de una serie
     de datos

    Argumentos:
        datos: lista con los datos

    Devuelve:
        resultado: densidad de probabilidad de los datos
    """
    # Se calculan los valores únicos para poder ver el número
    # de repeticiones
    datos_sinduplicados = list(set(datos))
    # Se aplica el peso de la frecuencia relativa a cada elemento único
    return [1 / len(datos) * datos.count(i) for i in datos_sinduplicados]


def calcula_media(datos):
    """Función que calcula la media de los valores dados

    Argumentos:
        datos: lista con los datos

    Devuelve:
        resultado: media de los datos
    """
    return sum(datos) / len(datos)


def estadisticas_basicas(fichero, columna, columna_filtro, filtro, mostrar=True):
    """Función que para un archivo dado y dos columnas, calcula los valores
     minimo, maximo, y media de la columna que cumplen todos los filtros
     indicados en la otra columna

    Argumentos:
        fichero: nombre del archivo a leer
        columna: nombre de la columna donde buscar
        columna_filtro: nombre de la columna que tendrá los filtros
        filtro: filtro que han de cumplir todos los elementos
        mostrar: indica si se muestran los resultados por pantalla. True por defecto

    Devuelve:
        maximo: valor máximo encontrado
        media: media calculada
        minimo: valor minimo encontrado
    """
    datos = filtra_columna(fichero, columna, columna_filtro, filtro)
    valores = [float(i) if i != "" else 0 for i in datos]
    num_maximo = max(valores)
    num_minimo = min(valores)
    media_calculada = calcula_media(valores)
    if mostrar:
        print(
            'Las estadísticas de "{}" filtradas para la columna "{}" con valor {} son:\n\tMáximo valor: {}'
            "\n\tMínimo valor: {}\n\tValor medio: {:.4f}".format(
                columna,
                columna_filtro,
                filtro,
                num_maximo,
                num_minimo,
                media_calculada,
            )
        )
    return media_calculada, num_minimo, num_maximo
