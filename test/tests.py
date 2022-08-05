import unittest

# Necesario para que Coverage pueda ejecutarse desde ./test en lugar
# desde el raíz del proyecto
import os
import sys
import inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import descubreartistas


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._a1 = [2, 5, 6, 5, 7, 8, 1]
        cls._b1 = [-155, 0, 1, 34, 5, 4, -7]
        cls._c1 = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5]
        cls._a2 = [434, 43, 34, 345, 53, 5, 1]
        cls._b2 = [-15, -2, 13, 34, 53, 31, -71]
        cls._c2 = [3, 4, 4, 3, 42, 0, 65, 1, 2, 5]
        cls._a3 = [4, 3, 2, 1, 3, -5, -1]
        cls._b3 = [5, -72, 3, 64, -12, 45, -7]
        cls._c3 = [5, 4, 5, 6, 2, 9, 8, 7, 7, 5, 6]
        cls._output = "./data/processed/tracks_denorm.csv"
        cls._csv = "./data/processed/artists_audiodb.csv"
        cls._zip_file = "./data/external/data.zip"
        cls._artist_file = "./data/interim/artists_norm.csv"
        cls._album_file = "./data/interim/albums_norm.csv"
        cls._tracks_file = "./data/interim/tracks_norm.csv"
        cls._fig1 = "./figuras/heatmap.png"
        cls._fig2 = "./figuras/densidad_probabilidad.png"
        cls._fig3 = "./figuras/compara.png"
        cls._fig4 = "./figuras/media.png"
        cls._fig5 = "./figuras/test_read.png"
        cls._columna1 = "speechiness"
        cls._columna2 = "artist_name"
        cls._columna3 = ["Ac/Dc"]
        cls._features = [
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
        cls._filtro2 = ["Ac/Dc", "Megadeth", "Metallica", "Slipknot"]
        cls._filtro3 = ["Marea", "Queen", "Coldplay", "Linkin Park"]
        cls._filtro4 = ["Adele", "Nirvana", "Aerosmith"]
        cls._columna4 = ["Marea"]
        cls._columna5 = ["Ac/Dc", "Megadeth"]
        cls._columna6 = "album_name"

    def test_denormalize_files(self):
        print("Starting test_denormalize_files")
        r1, r2, r3 = descubreartistas.denormalize_files(
            self._zip_file,
            self._artist_file,
            self._album_file,
            self._tracks_file,
            self._output,
            True,
        )
        self.assertEqual(r2, 35574)
        self.assertEqual(r3, 32)

    def test_similitud_euclidiana(self):
        print("Starting test_similitud_euclidiana")
        r1 = descubreartistas.similitud_euclidiana(self._a1, self._b1)
        r2 = descubreartistas.similitud_euclidiana(self._a2, self._b2)
        r3 = descubreartistas.similitud_euclidiana(self._a3, self._b3)
        self.assertEqual(r1, 0.41700342232805443)
        self.assertEqual(r2, 0.29799987098209707)
        self.assertEqual(r3, 0.17391614332394503)

    def test_similitud_cosinus(self):
        print("Starting test_similitud_cosinus")
        r1 = descubreartistas.similitud_cosinus(self._a1, self._b1)
        r2 = descubreartistas.similitud_cosinus(self._a2, self._b2)
        r3 = descubreartistas.similitud_cosinus(self._a3, self._b3)
        self.assertEqual(r1, 0.03259093571058569)
        self.assertEqual(r2, 0.14863532728869766)
        self.assertEqual(r3, -0.4389091163467491)

    def test_calcula_media(self):
        print("Starting test_calcula_media")
        r1 = descubreartistas.calcula_media(self._a1)
        r2 = descubreartistas.calcula_media(self._b1)
        r3 = descubreartistas.calcula_media(self._c1)
        self.assertEqual(r1, 4.857142857142857)
        self.assertEqual(r2, -16.857142857142858)
        self.assertEqual(r3, 2.5)

    def test_densidad_probabilidad(self):
        print("Starting test_calcula_media")
        r1 = descubreartistas.densidad_probabilidad(self._c1)
        r2 = descubreartistas.densidad_probabilidad(self._c2)
        r3 = descubreartistas.densidad_probabilidad(self._c3)
        self.assertEqual(r1, [0.1, 0.2, 0.2, 0.2, 0.2, 0.1])
        self.assertEqual(r2, [0.1, 0.1, 0.1, 0.2, 0.2, 0.1, 0.1, 0.1])
        self.assertEqual(
            r3,
            [
                0.09090909090909091,
                0.09090909090909091,
                0.2727272727272727,
                0.18181818181818182,
                0.18181818181818182,
                0.09090909090909091,
                0.09090909090909091,
            ],
        )

    def test_estadisticas_basicas(self):
        print("Starting test_estadisticas_basicas")
        r1, r2, r3 = descubreartistas.estadisticas_basicas(
            self._output, self._columna1, self._columna2, self._columna3, True
        )
        self.assertEqual(r1, 0.07092427983539094)
        self.assertEqual(r2, 0.0246)
        self.assertEqual(r3, 0.302)

    def test_mostrar_heatmap(self):
        print("Starting test_mostrar_heatmap")
        r1, r2 = descubreartistas.mostrar_heatmap(
            self._output,
            self._features,
            self._columna2,
            self._filtro2,
            self._fig1,
            True,
        )
        self.assertEqual(
            r1,
            [
                [1.0, 0.999945403206296, 0.999856989745573, 0.9999912331816413],
                [0.999945403206296, 1.0, 0.999802744671724, 0.9999379605707076],
                [0.999856989745573, 0.999802744671724, 1.0, 0.9998636370120537],
                [0.9999912331816413, 0.9999379605707076, 0.9998636370120537, 1.0],
            ],
        )
        self.assertEqual(
            r2,
            [
                [
                    0.9999999999999999,
                    0.999999999198776,
                    0.9999999955109878,
                    0.9999999999660393,
                ],
                [
                    0.999999999198776,
                    0.9999999999999999,
                    0.9999999909452305,
                    0.9999999988803134,
                ],
                [0.9999999955109878, 0.9999999909452305, 1.0, 0.9999999961233785],
                [
                    0.9999999999660393,
                    0.9999999988803134,
                    0.9999999961233785,
                    1.0000000000000002,
                ],
            ],
        )

    def test_hist_feature(self):
        print("Starting test_hist_feature")
        r1, r2 = descubreartistas.hist_feature(
            self._output,
            self._features[2],
            self._columna2,
            self._columna4,
            self._fig2,
            True,
        )
        self.assertEqual(r1[0], 6.0)
        self.assertEqual(r2[0], 0.009174311926605505)

    def test_compare_hist_feature(self):
        print("Starting test_compare_hist_feature")
        r1, r2 = descubreartistas.compare_hist_feature(
            self._output, self._features[2], self._columna2, self._columna5, self._fig3
        )
        self.assertEqual(r1[0][0], 7.0)
        self.assertEqual(r2[0][0], 0.00411522633744856)

    def test_maxima_coincidencia_filtrada(self):
        print("Starting test_compare_hist_feature")
        r1 = descubreartistas.maxima_coincidencia_filtrada(
            self._output, self._features[1], self._columna2, self._columna3
        )
        r2 = descubreartistas.maxima_coincidencia_filtrada(
            self._output, self._features[0], self._columna2, self._columna3
        )
        r3 = descubreartistas.maxima_coincidencia_filtrada(
            self._output, self._features[2], self._columna2, self._columna3
        )
        self.assertEqual(r1, 0.995)
        self.assertEqual(r2, 0.754)
        self.assertEqual(r3, 11.0)

    def test_grafico_media(self):
        print("Starting test_grafico_media")
        r1 = descubreartistas.grafico_media(
            self._output,
            self._features[0],
            self._columna6,
            self._columna2,
            self._columna3,
            self._fig4,
        )
        r2 = descubreartistas.grafico_media(
            self._output,
            self._features[1],
            self._columna6,
            self._columna2,
            self._columna3,
            self._fig4,
        )
        r3 = descubreartistas.grafico_media(
            self._output,
            self._features[1],
            self._columna6,
            self._columna2,
            self._columna4,
            self._fig4,
        )
        self.assertEqual(r1["Back In Black"], 0.4558999999999999)
        self.assertEqual(r2["Back In Black"], 0.8469000000000001)
        self.assertEqual(r3["El azogue"], 0.8585999999999998)

    def test_test_read(self):
        print("Starting test_test_read")
        r1, r2 = descubreartistas.test_read(
            [self._artist_file, self._album_file, self._tracks_file],
            ["artist_id", "album_id", "track_id"],
            self._fig5,
        )
        self.assertEqual(r1, [68, 2135, 35574])
        self.assertEqual(r2, [68, 2135, 35574])

    def test_recuperar_artistas(self):
        print("Starting test_recuperar_artistas")
        r1 = descubreartistas.recuperar_artistas(self._filtro2, self._csv)
        r2 = descubreartistas.recuperar_artistas(self._filtro3, self._csv)
        r3 = descubreartistas.recuperar_artistas(self._filtro4, self._csv)
        self.assertEqual(r1, 4)
        self.assertEqual(r2, 4)
        self.assertEqual(r3, 3)

    def test_multiples_filtros(self):
        print("Starting test_multiples_filtros")
        r1 = descubreartistas.multiples_filtros(
            self._output, self._features[1], self._columna2, self._columna5
        )
        r2 = descubreartistas.multiples_filtros(
            self._output, self._features[2], self._columna2, self._columna5
        )
        r3 = descubreartistas.multiples_filtros(
            self._output, self._features[0], self._columna2, self._columna5
        )
        self.assertEqual(len(r1), 93)
        self.assertEqual(len(r2), 12)
        self.assertEqual(len(r3), 111)

    def test_numero_coincidencias(self):
        print("Starting test_numero_coincidencias")
        r1 = descubreartistas.numero_coincidencias(
            self._output, "album_release_year", ["2020"], tipo="exacta"
        )
        r2 = descubreartistas.numero_coincidencias(
            self._output, "album_release_year", ["2019"], tipo="exacta"
        )
        r3 = descubreartistas.numero_coincidencias(
            self._output, "album_release_year", ["2018"], tipo="exacta"
        )
        self.assertEqual(r1, 1401)
        self.assertEqual(r2, 1163)
        self.assertEqual(r3, 1219)


if __name__ == "__main__":
    unittest.main()
