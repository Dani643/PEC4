import urllib.request
from urllib.parse import quote
import json
import time


def recuperar_artistas(artistas, fichero, mostrar=True):
    """Función que lee los datos de los artistas de la web audioDB
     y genera un fichero CSV con su nombre, fecha de creación del grupo
     y ciudad de origen

    Argumentos:
        artistas: lista con los artistas a buscar
        fichero: nombre del fichero CSV a generar
        mostrar: muestra opcionalmente los datos procesados

    Devuelve:
        número de artistas procesados
    """
    # Tiempo de espera marcado por la API necesario entre consultas
    espera_api = 2
    # Se crea el archivo de salida con la cabecera
    with open(fichero, "w") as out:
        out.write("artist_name;formed_year;country\n")
    # Se leen cada uno de los artistas desde audioDB
    for artista in artistas:
        # Se crea la url evitando problemas de espacios y codificación
        direccion = "https://theaudiodb.com/api/v1/json/2/search.php?s=" + quote(
            artista
        )
        with urllib.request.urlopen(direccion) as url:
            data = json.loads(url.read().decode())
        # Se escribe el artista o se evita si no se ha encontrado
        if data["artists"] is not None:
            anyo = ""
            ciudad = ""
            if data["artists"][0]["intFormedYear"] is not None:
                anyo = data["artists"][0]["intFormedYear"]
            if data["artists"][0]["strCountry"] is not None:
                ciudad = data["artists"][0]["strCountry"].split(",")[0]
            with open(fichero, "a") as out:
                out.write(artista + ";" + anyo + ";" + ciudad + "\n")
            if mostrar:
                print(artista, anyo, ciudad)
        time.sleep(espera_api)
    return len(artistas)
