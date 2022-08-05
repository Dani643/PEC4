from descubreartistas.columns.read import get_column_lines


def multiples_filtros(fichero, columna, columna_filtro, filtro, mostrar=True):
    """Función que para un archivo dado y dos columnas, devuelve los valores
     de la columna que cumplen todos los filtros marcados en la otra columna

    Argumentos:
        fichero: nombre del archivo a leer
        columna: nombre de la columna donde buscar
        columna_filtro: nombre de la columna que tendrá los filtros
        filtro: filtro que han de cumplir todos los elementos
        mostrar: imprime o no los resultados. True por defecto

    Devuelve:
        totales: elementos que cumplen todas las condiciones
    """
    # Se leen las filas
    filas_objetivo = get_column_lines(fichero, columna)
    filas_filtro = get_column_lines(fichero, columna_filtro)
    # Se crea una sola lista para poder trabajar con las dos a la vez
    filas_union = [[i, s] for i, s in zip(filas_objetivo, filas_filtro)]
    # Se crea un diccionario para mantener cada uno de los filtros individuales
    ocurrencias = dict()
    # Se rellena el diccionario
    for elemento_filtra in filtro:
        ocurrencias[elemento_filtra] = list(
            set([i[0] for i in filas_union if elemento_filtra in i[1]])
        )
    # Ahora es necesario verificar que elementos están en todos los filtros
    # Se selecciona por ejemplo el primer filtro para ver que elementos de este están en todos
    posibles = ocurrencias[filtro[0]]
    totales = []
    for i in posibles:
        # Solo se mantienen aquellos que están en todos los filtros
        if all(i in val for val in ocurrencias.values()):
            totales.append(i)
    if mostrar:
        print(
            'Los valores de "{}" que cumplen los filtros {} de la columna "{}" son: {}'.format(
                columna, filtro, columna_filtro, totales
            )
        )
    return totales


def maxima_coincidencia_filtrada(fichero, columna_maximo, columna_filtro, filtro):
    """Función que para un archivo dado y dos columnas, calcula el máximo
     valor de los valores de una columna aplicando previamente un filtrado
     en la otra columna según los elementos contenidos en filtro.
    Muestra los resultados por pantalla y devuelve el valor calculado

    Argumentos:
        fichero: nombre del archivo a leer
        columna_maximo: nombre de la columna donde buscar
        columna_filtro: nombre de la columna que filtra
        filtro: elementos por los que filtrar

    Devuelve:
        maximo: valor máximo calculado
    """
    # Se leen las filas
    filas_objetivo = get_column_lines(fichero, columna_maximo)
    filas_filtro = get_column_lines(fichero, columna_filtro)
    # Se crea una sola lista para poder trabajar con las dos a la vez
    filas_union = [[i, s] for i, s in zip(filas_objetivo, filas_filtro)]
    # Se calcula el máximo
    maximo = max([float(i[0]) for i in filas_union if i[1] in filtro])
    print(
        'El máximo valor de la columna "{}" filtrada por {} en la columna "{}" es: {}'.format(
            columna_maximo, filtro, columna_filtro, maximo
        )
    )
    return maximo


def numero_coincidencias(fichero, columna, coincidencia, tipo="exacta"):
    """Función que para un archivo dado y una columna calcula el número
     de coincidencias exactas o parciales de las palabras de una lista.
    Muestra los resultados por pantalla y devuelve el valor calculado

    Argumentos:
        fichero: nombre del archivo a leer
        columna: nombre de la columna donde buscar
        coincidencia: lista de los elementos que se buscan
        tipo: tipo de búsqueda, 'exacta' busca la palabra completa
                                'parcial' busca el contenido de la palabra
    Devuelve:
        resultado: valor calculado
    """
    resultado = 0
    for datos in coincidencia:
        filas = get_column_lines(fichero, columna)
        # Si la coincidencia es exacta se cuenta directamente
        if tipo == "exacta":
            resultado += filas.count(datos)
        # Se cuenta solo si está contenido el texto en la celda
        elif tipo == "parcial":
            resultado += len([i for i in filas if datos.upper() in i.upper()])
    print(
        'En la columna "{}" se han encontrado "{}" coincidencias de los elementos: {} '.format(
            columna, resultado, coincidencia
        )
    )
    return resultado


def filtra_columna(fichero, columna, columna_filtro, filtro):
    """Función que para un archivo dado y dos columnas, devuelve los valores
     de una columna aplicando previamente un filtrado en la otra columna
     según los elementos contenidos en filtro. Devuelve una lista con los
      valor resultantes

    Argumentos:
        fichero: nombre del archivo a leer
        columna: nombre de la columna donde buscar
        columna_filtro: nombre de la columna que filtra
        filtro: elementos por los que filtrar

    Devuelve:
        resultados: valor máximo calculado
    """
    # Se leen las filas
    filas_objetivo = get_column_lines(fichero, columna)
    filas_filtro = get_column_lines(fichero, columna_filtro)
    # Se crea una sola lista para poder trabajar con las dos a la vez
    filas_union = [[i, s] for i, s in zip(filas_objetivo, filas_filtro)]
    # Se devuelve el resultado asegurando que si el elemento a filtrar es único,
    # no se está devolviendo un nombre que está contenido en el filtro, y si es
    # una lista que esté contenida en la lista
    if len(filtro) == 1:
        return [i[0] for i in filas_union if i[1] == filtro[0]]
    else:
        return [i[0] for i in filas_union if i[1] in filtro]
