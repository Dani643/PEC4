import descubreartistas
from threading import Thread
import matplotlib.pyplot as plt

# Variables Tarea 1
zip_file = "./data/external/data.zip"
artist_file = "./data/interim/artists_norm.csv"
album_file = "./data/interim/albums_norm.csv"
tracks_file = "./data/interim/tracks_norm.csv"
output_file = "./data/processed/tracks_denorm.csv"

# Variables Tarea 2
list_files = [artist_file, album_file, tracks_file]
column_names = ["artist_id", "album_id", "track_id"]
test_read = "./reports/figures/test_read.png"

# Variables Tarea 4.B
media_file = "./reports/figures/media_feature.png"

# Variables Tarea 5
densidad_file = "./reports/figures/densidad_probabilidad.png"

# Variables Tarea 6
compara_file = "./reports/figures/comparacion_histogramas.png"


# Variables Tarea 7
# Listado de las features a analizar
features_analizar = [
    "danceability",
    "energy",
    "key",
    "loudness",
    "mode",
    "speechiness",
    "acousticness",
    "instrumentalness",
    "liveness",
    "valence",
    "tempo",
    "duration_ms",
]
heatmap_file = "./reports/figures/heatmaps.png"

# Variables Tarea 8
datos_file = "./data/processed/artists_audiodb.csv"

if __name__ == "__main__":

    # Tarea 8.Evaluación
    print("\nTarea 8.Evaluación")
    artistas = list(set(descubreartistas.get_column_lines(output_file, "artist_name")))
    # Creamos el thread
    thread = Thread(
        target=descubreartistas.recuperar_artistas, args=(artistas, datos_file, False)
    )
    # Ejecutamos el thread
    thread.start()
    print("\tTarea 8.Evaluación: Comienza el proceso")

    # Tarea 1
    print("Tarea 1")
    descubreartistas.denormalize_files(
        zip_file, artist_file, album_file, tracks_file, output_file
    )

    # Tarea 2
    print("\nTarea 2: Se genera grafica")
    descubreartistas.test_read(list_files, column_names, test_read)

    # Tarea 3.A
    print("\nTarea 3.A")
    descubreartistas.numero_coincidencias(
        output_file, "artist_name", ["Radiohead", "Adele"]
    )
    # Tarea 3.B
    print("\nTarea 3.B")
    descubreartistas.numero_coincidencias(
        output_file, "name", ["police"], tipo="parcial"
    )
    # Tarea 3.C
    print("\nTarea 3.C")
    descubreartistas.numero_coincidencias(
        output_file, "album_release_year", [str(x) for x in range(1990, 2000)]
    )
    # Tarea 3.D
    print("\nTarea 3.D")
    descubreartistas.maxima_coincidencia_filtrada(
        output_file,
        "popularity",
        "album_release_year",
        [str(x) for x in range(2011, 2022)],
    )
    # Tarea 3.E
    print("\nTarea 3.E")
    descubreartistas.multiples_filtros(
        output_file,
        "artist_name",
        "album_release_year",
        [str(x) for x in range(196, 203)],
    )

    # Tarea 4.A
    print("\nTarea 4.A")
    descubreartistas.estadisticas_basicas(
        output_file, "energy", "artist_name", ["Metallica"]
    )

    # Tarea 4.B
    print("\nTarea 4B: Se genera gráfica")
    descubreartistas.grafico_media(
        output_file,
        "danceability",
        "album_name",
        "artist_name",
        ["Coldplay"],
        media_file,
    )

    # Tarea 5
    print("\nTarea 5: Se genera gráfica")
    descubreartistas.hist_feature(
        output_file, "acousticness", "artist_name", ["Ed Sheeran"], densidad_file
    )

    # Tarea 6
    print("\nTarea 6: Se genera gráfica")
    descubreartistas.compare_hist_feature(
        output_file, "energy", "artist_name", ["Adele", "Extremoduro"], compara_file
    )

    # Tarea 7
    print("\nTarea 7: Se genera gráfica")
    descubreartistas.mostrar_heatmap(
        output_file,
        features_analizar,
        "artist_name",
        ["Metallica", "Extremoduro", "Ac/Dc", "Hans Zimmer"],
        heatmap_file,
    )

    # Tarea 8
    print("\nTarea 8: Se genera fichero")
    descubreartistas.recuperar_artistas(
        ["Radiohead", "David Bowie", "Måneskin"], datos_file
    )

    # Fin Tarea 8.Evaluación
    thread.join()

    print("\n\tTarea 8.Evaluación: Finaliza la evaluación")
    print(
        "\tLa implementación de la tarea 8 ha sido eficiente ya que se ha ejecutado en un hilo independiente,\n"
        "\tlo que ha permitido que se ejecuten el resto de las tareas de validación en paralelo. Así se mejora el\n"
        "\ttiempo global ya que como la API de audioDB marca que es necesario esperar 2 segundos por consulta, y el\n"
        "\ttiempo de ejecución total ha sido de aproximadamente 140 segundos (casi 70 artistas por 2 segundos),\n"
        "\timplica que todas las tareas se han podido realizar mientras que se recuperaban los datos en remoto.\n"
        "\tSi la aplicación tiene que escalar para realizar miles de consultas se mantendrá la restricción de la API\n"
        "\tde audioDB, por lo que los tiempos de espera seguirán existiendo, así que esta implementación continuaría\n"
        "\tsiendo valida, ya que se aprovecharían los tiempos de recuperación de los datos para poder continuar con\n"
        "\tel proceso normal mediante el resto de funciones aportadas por el paquete."
    )
    # Se muestran todos los gráficos generados pendientes de mostrar
    # para evitar bloqueos en la ejecución
    plt.show()
