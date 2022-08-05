from descubreartistas.audiofeatures.analisis import *
import seaborn as sns
import matplotlib.pylab as plt


def mostrar_heatmap(fichero, features, columna_filtro, filtro, salida, mostrar=True):
    """Función que muestra dos heatmaps comparando los elementos de la
     columna columna_filtro indicados en filtro, mediante el procesado
    de las features indicadas

    Argumentos:
        fichero: nombre del archivo a leer
        feature: valores para componer el vector para procesar
        columna_filtro: nombre de la columna que filtrará
        filtro: filtro que han de cumplir los elementos de columna_filtro
        salida: nombre del archivo a escribir
        mostrar: muestra y guarda el heatmap

    Devuelve:
        matriz_cosinus: matriz coseno creada
        matriz_euclediana: matriz euclediana creada
        heatmaps.png: se crea un fichero con el gráfico
    """
    participantes = dict()

    # Se calcula la media de cada una de las features para cada uno de los
    # elementos que existen en filtro
    for filtrado in filtro:
        participantes[filtrado] = []
        for columna in features:
            num_media, num_minimo, num_maximo = estadisticas_basicas(
                fichero, columna, columna_filtro, filtrado, False
            )
            participantes[filtrado].append(num_media)
    # Para cada uno de los vectores generados, se calcula la similitud
    # Euclediana y Cosinus respecto de cada uno de esos mismos vectores
    matriz_euclediana = []
    matriz_cosinus = []
    for datos_a in filtro:
        temporal_euclediana = []
        temporal_cosinus = []
        for datos_b in filtro:
            temporal_euclediana.append(
                similitud_euclidiana(participantes[datos_a], participantes[datos_b])
            )
            temporal_cosinus.append(
                similitud_cosinus(participantes[datos_a], participantes[datos_b])
            )
        matriz_euclediana.append(temporal_euclediana)
        matriz_cosinus.append(temporal_cosinus)
    if mostrar:
        # Se muestran y guardan los dos Heatmaps para comparar cada metodo
        fig, (ax1, ax2) = plt.subplots(figsize=(20, 5), ncols=2)
        sns.heatmap(
            matriz_euclediana,
            linewidth=0.5,
            yticklabels=filtro,
            xticklabels=filtro,
            ax=ax1,
        )
        ax1.set_yticklabels(filtro, rotation=0)
        ax1.set_title("Matriz Euclediana")
        sns.heatmap(
            matriz_cosinus,
            linewidth=0.5,
            yticklabels=filtro,
            xticklabels=filtro,
            ax=ax2,
        )
        ax2.set_yticklabels(filtro, rotation=0)
        ax2.set_title("Matriz Cosinus")
        fig.tight_layout()
        plt.show(block=False)
        fig.savefig(salida)
    return matriz_euclediana, matriz_cosinus
