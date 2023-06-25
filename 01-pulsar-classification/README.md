# Pulsar Classification For Class Prediction

https://www.kaggle.com/datasets/brsdincer/pulsar-classification-for-class-prediction

## Ambiente Virtual

Crear ambiente virtual para desarrollo de proyecto ML.
Crear archivo `conda.yaml` con las librerias necesirias para desarrollar el proyecto.

    conda env create -f conda.yaml

    conda activate datapath_py01

    ipython kernel install --user --name=py01
    
Salir de entorno
    
    conda deactivate

Remover entorno

    conda env remove --name datapath_py01 --all

## Datos

Descargar datos

    mkdir data
    cd data
    kaggle datasets download -d brsdincer/pulsar-classification-for-class-prediction

## EDA

Realizar análisis exploratorio de variables, limpieza de datos, feature engineering, feature selection.

    my_notebook.ipynb

## Entrenamiento del modelo

Realizar el entrenamiento del modelo ML: train, test, validación.

    my_notebook.ipynb

Se genera un archivo `main.py` que genere solo la predicción.

## Deploy

Generar los archivos que garanticen la reproducibilidad del modelo y su puesta en producción:

conda.yaml
requirements.txt
Dockerfile

## Github

Ir generando los commits para evidenciar los avances del proyecto

    git commit

Los archivos del proyecto se encuentran en:

    https://github.com/alangrosso/datapath-mle/tree/main/proyecto01

