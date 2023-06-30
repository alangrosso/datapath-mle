# **Pulsar Classification For Class Prediction - API**

https://www.kaggle.com/datasets/brsdincer/pulsar-classification-for-class-prediction

## **Ambiente Virtual**

En el archivo `conda.yaml` agregar las librerias necesarias para desarrollar el proyecto.

Crear ambiente virtual:

    conda env create -f conda.yaml

    conda activate datapath_py02

    ipython kernel install --user --name=py02
    
Salir de entorno:
    
    conda deactivate

Remover entorno:

    conda env remove --name datapath_py02 --all

## **Estructura del proyecto**

Files necesarios:

```
├── README.md
├── artifacts
│   ├── model.joblib
│   └── scaler.joblib
├── conda.yaml
├── controllers
│   └── ml_controller.py
├── images
│   ├── 01_post.PNG
│   ├── 02_get.PNG
│   ├── 03_put.PNG
│   └── 04_delete.PNG
├── main.py
├── models
│   └── models.py
├── my_notebook.ipynb
├── routers
│   └── routes.py
```

## **Requirements**

Generar los archivos que garanticen la reproducibilidad del modelo y su puesta en producción:

    environment.yaml (conda env export > environment.yml)
    requirements.txt (pip list --format=freeze > requirements.txt, conda list -e > requirements.txt)

## **Probar API**

Ejecutar servidor:

    uvicorn main:app --reload

Verificar métodos en directorio `images`.

## **Github**

Generar los commits para evidenciar los avances del proyecto:

    Crear repo

    git init
    git pull

    git branch dev
    git checkout dev

    git add .
    git commit -m "primera commit api para modelo ml"
    git push origin dev

Merge con rama main:

    git checkout main
    git merge dev -m "merge dev sin conflictos"

Link del repo:

    https://github.com/alangrosso/datapath-mle/tree/main/02-pulsar-api
    