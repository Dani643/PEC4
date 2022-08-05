from descubreartistas.columns.read import *
import time
import matplotlib.pyplot as plt


def test_read(list_files, columnas, salida):
    """Función que para una lista de archivos y de columnas, realiza las
    lecturas de las mismas por dos métodos distintos y muestra una gráfica
    comparativa de los resultados

    Argumentos:
        list_files: lista de los archivos a leer
        columnas: lista de las columnas a leer que corresponden una a una
                    con el nombre de los ficheros
        salida: nombre del archivo a escribir

    Devuelve:
        elementos_pandas: número elementos leídos con pandas
        elementos_lines: número elementos mediante lines
    """
    tiempos_pandas = []
    tiempos_lines = []
    elementos_pandas = []
    elementos_lines = []
    for ind, file in enumerate(list_files):
        # Prueba con un fichero para la lectura por pandas
        start_time = time.time()
        elementos_pandas.append(len(get_column_pandas(file, columnas[ind])))
        tiempos_pandas.append(time.time() - start_time)

        # Prueba con un fichero para la lectura por líneas
        start_time = time.time()
        elementos_lines.append(len(get_column_lines(file, columnas[ind])))
        tiempos_lines.append(time.time() - start_time)

    # Se pinta la gráfica, se le da formato y se guarda
    fig = plt.figure()
    plt.plot(
        elementos_pandas,
        tiempos_pandas,
        color="green",
        linestyle="dashed",
        linewidth=2,
        marker="o",
        markerfacecolor="blue",
        markersize=10,
        label="Pandas",
    )
    plt.plot(
        elementos_lines,
        tiempos_lines,
        color="brown",
        linestyle="dashed",
        linewidth=2,
        marker="o",
        markerfacecolor="red",
        markersize=6,
        label="Líneas",
    )
    plt.xlabel("Número de líneas leídas")
    plt.ylabel("Tiempo de ejecución en segundos")
    plt.title("Comparación de lectura por pandas y por líneas")
    plt.legend(loc="upper center")
    plt.show(block=False)
    fig.savefig(salida)
    return elementos_pandas, elementos_lines
