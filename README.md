<<<<<<< HEAD
# Pyros API - Railway Deployment

Esta es la API de FastAPI para el proyecto Pyros, desplegada en Railway.

## Archivos necesarios para el despliegue

1. **api.py** - Servidor FastAPI principal
2. **car_make_model_classifier_yolo3.py** - Lógica de procesamiento de imágenes
3. **classifier.py** - Clasificador de modelos de coches
4. **config.py** - Configuración del proyecto
5. **yolo-coco/** - Carpeta con archivos del modelo YOLO
   - yolov3.weights
   - yolov3.cfg
   - coco.names
6. **model-weights-spectrico-mmr-mobilenet-128x128-344FF72B.pb** - Modelo de clasificación

## Instrucciones de despliegue

1. Sube todos los archivos de esta carpeta a tu repositorio de GitHub
2. Conecta el repositorio a Railway
3. Railway detectará automáticamente que es una aplicación Python
4. La API estará disponible en la URL proporcionada por Railway

## Endpoints

- `POST /procesar-imagen/` - Procesa una imagen y devuelve información del coche detectado

## Variables de entorno

=======
# Pyros API - Railway Deployment

Esta es la API de FastAPI para el proyecto Pyros, desplegada en Railway.

## Archivos necesarios para el despliegue

1. **api.py** - Servidor FastAPI principal
2. **car_make_model_classifier_yolo3.py** - Lógica de procesamiento de imágenes
3. **classifier.py** - Clasificador de modelos de coches
4. **config.py** - Configuración del proyecto
5. **yolo-coco/** - Carpeta con archivos del modelo YOLO
   - yolov3.weights
   - yolov3.cfg
   - coco.names
6. **model-weights-spectrico-mmr-mobilenet-128x128-344FF72B.pb** - Modelo de clasificación

## Instrucciones de despliegue

1. Sube todos los archivos de esta carpeta a tu repositorio de GitHub
2. Conecta el repositorio a Railway
3. Railway detectará automáticamente que es una aplicación Python
4. La API estará disponible en la URL proporcionada por Railway

## Endpoints

- `POST /procesar-imagen/` - Procesa una imagen y devuelve información del coche detectado

## Variables de entorno

>>>>>>> fb0ea5fde6937f66d5b654a46c946eea92c611d4
No se requieren variables de entorno adicionales para este despliegue. 