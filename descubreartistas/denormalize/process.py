import zipfile as zf
import pandas as pd


def denormalize_files(
    zip_file, artist_file, album_file, tracks_file, output_file, mostrar=True
):
    """Función que dado un archivo zip, descomprime los ficheros, y los
    des-normaliza según los nombres indicados. Muestra los valores
    totales de tracks, de columnas y el número de tracks sin datos de
    popularity. También cambia los valores de popularity por la media de
    todos los del fichero y corrige los valores de los nombres de grupos
    cuya primera letra no está en mayúscula. Una vez procesado generará
    un fichero con los datos generados

    Esta función acepta 5 parámetros, con los nombres de los ficheros.

    Argumentos:
        zip_file: nombre del zip con los archivos
        artist_file: nombre del fichero que tendrá los datos de los artistas
        album_file: nombre del fichero que tendrá los datos de los álbumes
        tracks_file: nombre del fichero que tendrá los datos de los tracks
        output_file: nombre del fichero a escribir
        mostrar: mostrar resumen de los datos construidos. True por defecto

    Devuelve:
        df: datos desnormalizados
        total_tracks: número de filas del fichero resultante
        total_columnas: número de columnas del fichero resultante
    """
    # Se abre el archivo zip en modo de lectura
    with zf.ZipFile(zip_file, "r") as zip_f:
        # Se descomprimen los archivos
        zip_f.extractall(path="./data/interim/")
    # Se leen los ficheros
    artist_df = pd.read_csv(artist_file, sep=";")
    album_df = pd.read_csv(album_file, sep=";")
    tracks_df = pd.read_csv(tracks_file, sep=";")

    # Se corrigen los nombres de artistas incorrectos
    for index, artista in artist_df["name"].iteritems():
        artist_df.loc[index, "name"] = artista.title()

    # Se modifican los nombres de las columnas para que se pueda distinguir
    # entre el nombre del artista y del album al des-normalizar los datos
    for name in artist_df.columns:
        if name.find("artist") == -1:
            artist_df = artist_df.rename(columns={name: "artist_" + name})
    for name in album_df.columns:
        if name.find("album") == -1 and name.find("artist") == -1:
            album_df = album_df.rename(columns={name: "album_" + name})

    # Se des-normalizan los datos teniendo en cuenta que no se
    # quiere duplicar la columna artist_id al hacer el merge
    df = pd.merge(
        tracks_df,
        pd.merge(album_df, artist_df, on="artist_id").drop(["artist_id"], axis=1),
        on="album_id",
    )
    total_tracks = df["track_id"].count()
    total_columnas = len(df.columns)
    if mostrar:
        # Se añade el valor medio a aquellos valores de popularity vacíos
        df.loc[df["popularity"].isna(), "popularity"] = round(
            df["popularity"].mean(), 1
        )

        print("El número total de tracks es: {}".format(total_tracks))
        print(
            "El número de columnas del datasheet procesado es: {}".format(
                len(df.columns)
            )
        )
        print(
            "El número de tracks sin valor de popularity es: {}".format(
                tracks_df["popularity"].isna().sum()
            )
        )
    # Se crea el nuevo fichero CSV manteniendo el separador de los ficheros originales
    df.to_csv(output_file, sep=";", index=False)
    return df, total_tracks, total_columnas
