# **Airflow for ML Engineers**

## **Construir un DAG (Pipeline)**

1. Crear 2 tablas.
2. Inserta datos en las tablas.
3. Ambas tablas deben contar con una column Key en común.
4. Hacer un Join de las tablas.
5. Realizar una consulta con alguna condición (WHERE).

## **Configuración**

Ubicarse en la rama de desarrollo y crear directorio de trabajo:

    git branch
    git checkout dev
    mkdir 03-airflow-database
    cd 03-airflow-database
    mkdir -p ./dags ./logs ./plugins ./config ./databases

Variables de entorno:

    .env

Crear ambiente virtual e instalar librerias:

    python3.10 -m venv py_env
    source py_env/bin/activate
    pip install -r requirements.txt
    
Configuración Docker:

    docker-compose.yaml

Configuración base de datos:

    databases/docker-database.yaml

## **Desarrollo**

Directorio de trabajo:

    03-airflow-database$

Crear servicio:

    docker-compose up airflow-init

Configuración de permisos:

    sudo chmod 666 /var/run/docker.sock

Iniciar servicios ya creados:

    docker-compose up -d
    
Instalar base de datos sobre Docker:

    cd databases
    docker-compose -f docker-database.yaml up -d

Desarrollo de dags y tasks:

    dags/dag_with_postgres.py

Link Airflow:

    http://localhost:8080/

## **Resultados**

Verificar que las tareas planificadas se hayan ejecutado adecuadamente: `images`.

    ![](https://github.com/alangrosso/datapath-mle/blob/1309e6e0fc6dbfd7b938d5656c08126081fdaf81/03-airflow-database/images/01_dag.PNG)

    ![](https://github.com/alangrosso/datapath-mle/blob/1309e6e0fc6dbfd7b938d5656c08126081fdaf81/03-airflow-database/images/02_output.PNG) 

## **Github**

Generar los commits para evidenciar los avances del proyecto:

    Crear repo

    git init
    git pull

    git branch dev
    git checkout dev

    git add .
    git commit -m "primer commit airflow-database"
    git push origin dev

Merge con rama main:

    git checkout main
    git merge dev -m "merge dev sin conflictos"

## **Link del repo**

    https://github.com/alangrosso/datapath-mle/tree/main/03-airflow-database
    