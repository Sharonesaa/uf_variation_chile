# Variación UF

Este proyecto es una API construida con **FastAPI** para consultar la variación mensual de la UF (Unidad de Fomento) a lo largo de un año. Para ejecutar este proyecto, necesitas tener **Docker** instalado en tu máquina.

## Requisitos

1. Tener **Docker** instalado en tu sistema. Si no lo tienes, sigue las instrucciones de instalación en:  
   [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)

## Instrucciones para ejecutar el proyecto

1. En la raíz del proyecto, ejecuta el siguiente comando para iniciar el contenedor con Docker Compose:
    ```bash
    docker-compose up
   ```

    Esto construirá y levantará los contenedores necesarios para ejecutar el proyecto.

2. Si los contenedores no inician automáticamente, puedes intentar iniciar los contenedores con:
    ```bash
    docker-compose start
    ```
3. Para detener el proyecto, utiliza:

    ```bash
    docker-compose stop
    ```

## Rutas disponibles

Una vez que el contenedor esté en funcionamiento, podrás acceder a las siguientes rutas:

1. Formulario interactivo para consultar la variación UF
* URL: http://localhost:8000/uf-variation
* Esta ruta muestra un formulario donde puedes ingresar el año y obtener los resultados de la variación de la UF para ese año. Los resultados incluyen el valor mínimo y máximo de la UF, así como los meses en los que la UF subió, bajó o no tuvo variación.

2. Documentación interactiva de la API
* URL: http://localhost:8000/docs
* Esta ruta proporciona la documentación generada automáticamente por FastAPI para explorar las rutas de la API, ver los parámetros de entrada y las respuestas de la API de manera interactiva.

## Notas

* Si tienes algún problema o duda, por favor revisa los logs del contenedor con el siguiente comando:

    ```bash
    docker-compose logs
    ```
* Para más detalles sobre cómo trabajar con Docker Compose o FastAPI, consulta sus respectivas documentaciones:

    * Docker Compose: https://docs.docker.com/compose/
    * FastAPI: https://fastapi.tiangolo.com/


Este archivo `README.md` proporciona instrucciones claras para ejecutar y usar el proyecto, así como los detalles sobre las rutas disponibles para interactuar con la API.

