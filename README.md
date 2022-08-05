# Introducción al proyecto "PEC4" y el paquete "descubreartistas"

El proyecto "PEC4" se presenta como la interfaz principal para el desarrollo inicial del paquete "descubreartistas" de forma que se puedan probar los primeros módulos y funciones que se requieren para el proyecto que ha encargado la empresa UOC Sound Dynamics.

PEC4 contiene el paquete desarrollado, así como las herramientas para poder usarlo y testearlo adecuadamente, por lo que a continuación se indicará la forma en la que se puede proceder para estos objetivos.

El paquete "descubreartistas" está dividido en cinco partes:

* Audiofeatures: se trata de aquellos módulos que contienen funciones para analizar y presentar gráficas relacionadas con las audio features.
* Columns: para la lectura de columnas de los ficheros CSV brutos.
* Denormalize: para realizar la des-normalización de los ficheros originales y generar un solo fichero único.
* Filter: con funciones que se encargan de realizar todo tipo de filtrados en los datos.
* Retrieve: para recuperar datos de los artistas de la web de audioDB.

La estructura seguida para el proyecto está basada en Cookiecutter (https://drivendata.github.io/cookiecutter-data-science/#directory-structure) y es la siguiente:

```
PEC4
├── LICENSE       		- Fichero de licencia
├── main.py       		- Script para validar los requerimientos
├── README.md       		- Este fichero explicativo
├── requirements.txt       	- Librerías necesarias para ejecutar el paquete
├── setup.py           		- Archivo para hacer el paquete instalable
│
├── data
│   ├── external       		- Datos de entrada para el proyecto
│   ├── interim        		- Archivos intermedios generados en el proceso
│   └── processed      		- Archivos generados para usarse
│
├── descubreartistas   		- Código fuente del paquete
│   ├── __init__.py    		- Indicación de paquete Python
│   │
│   ├── audiofeatures  		- Código para trabajar con audiofeatures
│   │   ├── __init__.py		- Indicación de paquete Python
│   │   ├── analisis.py		- Funciones para el análisis de features
│   │   ├── graficos.py		- Módulo para mostrar gráficos de features
│   │   └── heatmaps.py		- Módulo para mostrar heatmaps de las features
│   │
│   ├── columns  		- Código para leer columnas de los ficheros
│   │   ├── __init__.py		- Indicación de paquete Python
│   │   ├── read.py		- Funciones para leer las columnas
│   │   └── test.py		- Módulo para realizar test de velocidad de lectura
│   ├── denormalize  		- Código para desnormalizar los ficheros
│   │   ├── __init__.py		- Indicación de paquete Python
│   │   └── process.py		- Contiene las funciones necesarias para el proceso de desnormalización
│   ├── filter  		- Código para realizar filtros en columnas
│   │   ├── __init__.py		- Indicación de paquete Python
│   │   └── funciones.py	- Funciones para filtrar los datos por una o varias columnas, valores, etc..
│   └── retrieve  		- Código para recuperar datos de artistas en remoto en audioDB
│       ├── __init__.py		- Indicación de paquete Python
│       └── data.py		- Modulo para leer de audioDB datos de artistas
│
├── reports            		- Reportes a generar en el proceso
│   └── figures        		- Gráficos generados durante el proceso
│
└── test            		- Test para el paquete descubreartistas
    ├── htmlcov    		- Informe de ejecución de los test mediante coverage
    └── tests.py	        - Fichero con la definición de los test
```

## Validación de requisitos

Para poder validar los requisitos incluidos mediante el listado de criterios de aceptación, se ha incluido un script llamado "./main.py" que ejecutará las funciones necesarias para que se muestren por pantalla los resultados para cada una de las diversas tareas.

Se puede probar ejecutandolo directamente mediante:

```
datasci@datasci:~/PycharmProjects/PEC4$ python main.py
```

Con la ejecución se mostrará por pantalla los resultados en formato texto cuando es posible, y en el resto de casos su respresentación gráfica. Además se generarán las gráficas en ficheros png guardados en el directorio indicado en la estructura (./reports/figures).



## Tests del paquete

Se han realizado tests a las funciones y módulos del paquete, por lo que se ha generado un fichero para realizar las ejecuciones de los mismos, que se encuentra en "./test/tests.py"

Se pueden lanzar mediante los siguientes comandos:

```
datasci@datasci:~/PycharmProjects/PEC4$ cd test
datasci@datasci:~/PycharmProjects/PEC4/test$ python -m unittest tests.py
```

O directamente a través de coverage:

```
datasci@datasci:~/PycharmProjects/PEC4$ cd test
datasci@datasci:~/PycharmProjects/PEC4/test$ coverage run -m unittest discover
```

Se ha generado de igual manera un html con el informe de resultados de cobertura que se encuentra en "./test/htmlcov/index.html"
A modo de resumen, en la última ejecución este fue el resultado:

```

Name                                                                            Stmts   Miss  Cover
---------------------------------------------------------------------------------------------------
/home/datasci/PycharmProjects/PEC4/descubreartistas/__init__.py                    10      0   100%
/home/datasci/PycharmProjects/PEC4/descubreartistas/audiofeatures/__init__.py       3      0   100%
/home/datasci/PycharmProjects/PEC4/descubreartistas/audiofeatures/analisis.py      42      0   100%
/home/datasci/PycharmProjects/PEC4/descubreartistas/audiofeatures/graficos.py      48      0   100%
/home/datasci/PycharmProjects/PEC4/descubreartistas/audiofeatures/heatmaps.py      32      0   100%
/home/datasci/PycharmProjects/PEC4/descubreartistas/columns/__init__.py             2      0   100%
/home/datasci/PycharmProjects/PEC4/descubreartistas/columns/read.py                16      0   100%
/home/datasci/PycharmProjects/PEC4/descubreartistas/columns/test.py                25      0   100%
/home/datasci/PycharmProjects/PEC4/descubreartistas/denormalize/__init__.py         1      0   100%
/home/datasci/PycharmProjects/PEC4/descubreartistas/denormalize/process.py         26      0   100%
/home/datasci/PycharmProjects/PEC4/descubreartistas/filter/__init__.py              1      0   100%
/home/datasci/PycharmProjects/PEC4/descubreartistas/filter/functions.py            40      2    95%
/home/datasci/PycharmProjects/PEC4/descubreartistas/retrieve/__init__.py            1      0   100%
/home/datasci/PycharmProjects/PEC4/descubreartistas/retrieve/data.py               25      0   100%
tests.py                                                                          146      1    99%
---------------------------------------------------------------------------------------------------
TOTAL                                                                             418      3    99%



```

## Conexión a la API de audioDB

Se ha implementado la funcionalidad necesaria para conectarse a la web de audioDB y recuperar datos de los artistas. La API presenta la limitación de no poder recibir más de 1 llamada cada 2 segundos (https://theaudiodb.com/api_guide.php), por lo que se ha aplicado esta restricción para evitar bloqueos por parte de la web.

Para que la implementación de la función de acceso sea optima, se ha de realizar a través de hilos, de manera que en un hilo pueden correr las llamadas a la API, mientras que el resto de funciones del programa pueden correr en paralelo, no viéndose bloqueadas por los tiempos de espera necesarios.

Un ejemplo de esto se encuentra en el script "./main.py" incluido en el proyecto.

De esta forma la escalabilidad se podrá respetar, de manera que, si es necesario buscar miles de artistas, el programa principal pueda seguir trabajando con los datos mientras que se recuperan los valores de los distintos artistas.

