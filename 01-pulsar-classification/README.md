# **Pulsar Classification For Class Prediction**

https://www.kaggle.com/datasets/brsdincer/pulsar-classification-for-class-prediction

## **Ambiente Virtual**

En el archivo `conda.yaml` agregar las librerias necesarias para desarrollar el proyecto.

Crear ambiente virtual:

    conda env create -f conda.yaml

    conda activate datapath_py01

    ipython kernel install --user --name=py01
    
Salir de entorno:
    
    conda deactivate

Remover entorno:

    conda env remove --name datapath_py01 --all

## **Datos**

Descargar datos:

    mkdir data
    cd data
    kaggle datasets download -d brsdincer/pulsar-classification-for-class-prediction

## **EDA**

Realizar análisis exploratorio de variables, limpieza de datos, feature engineering, feature selection.

    my_notebook.ipynb

## **Entrenamiento del modelo**

Realizar el entrenamiento del modelo ML: train, test, validación:

    my_notebook.ipynb

Se genera el archivo que genere solo la predicción:

    main.py

Obtener la predicción por línea de comandos:

    python main.py 0.7439 0.6277 0.2066 0.0264 0.1152 0.4540

Resultado:

    Mean_Integrated = 0.7439
    SD = 0.6277
    EK = 0.2066
    Mean_DMSNR_Curve = 0.0264
    SD_DMSNR_Curve = 0.1152
    EK_DMSNR_Curve = 0.4540
    Prediction: 0.013

## **Deploy**

Generar los archivos que garanticen la reproducibilidad del modelo y su puesta en producción:

    environment.yaml (conda env export > environment.yml)
    requirements.txt (pip list --format=freeze > requirements.txt, conda list -e > requirements.txt)
    Dockerfile

Generar la imagen de Docker:

    docker build -t pulsar_image .
    docker run pulsar_image 0.7439 0.6277 0.2066 0.0264 0.1152 0.4540

## **Github**

Generar los commits para evidenciar los avances del proyecto:

    Crear repo

    git init
    git pull

    git branch dev
    git checkout dev

    git add .
    git commit -m "proceso de machine learning"
    git push origin dev

    git add .
    git commit -m "archivo main.py"
    git push origin dev

    git add .
    git commit -m "archivo Dockerfile"
    git push origin dev

Merge con rama main:

    git checkout main
    git merge dev -m "merge dev sin conflictos"

Link del repo:

    https://github.com/alangrosso/datapath-mle/tree/main/01-pulsar-classification

