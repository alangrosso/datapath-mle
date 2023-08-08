# **MLOps**

Machine Learning pipeline:

`1. Read Data`➙`2. Split train-test`➙`3. Preprocess Data`➙`4. Train Model`➙<br>
&emsp; &emsp; &emsp; ➙ `5.1 Register Model`<br>
&emsp; &emsp; &emsp; ➙ `5.2 Update Registered Model`<br>

Telco Customer Churn dataset: <a href="https://www.kaggle.com/datasets/blastchar/telco-customer-churn" target="_blank">Kaggle</a>.

## **Tech Stack**
<a href="https://mlflow.org/" target="_blank"><img alt="MLflow" src="https://img.shields.io/badge/-MLflow-0194E2?style=flat-square&logo=mlflow&logoColor=white" height="20"/></a>: For experiment tracking and model registration<br>
<a href="https://www.postgresql.org/" target="_blank"><img alt="PostgreSQL" src="https://img.shields.io/badge/-PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white" height="20"/></a>: Store the MLflow tracking<br>
<a href="https://aws.amazon.com/s3/" target="_blank"><img alt="Amazon S3" src="https://img.shields.io/badge/-Amazon S3-569A31?style=flat-square&logo=amazons3&logoColor=white" height="20"/></a>: Store the artifacts and registered MLflow models<br>
<a href="https://aws.amazon.com/ecr/" target="_blank"><img alt="Amazon ECR" src="https://img.shields.io/badge/-Amazon%20ECR-569A31?style=flat-square&logo=amazon&logoColor=white" height="20"/></a>: Container registry<br>
<a href="https://aws.amazon.com/sagemaker/" target="_blank"><img alt="Amazon Sagemaker" src="https://img.shields.io/badge/-Amazon%20Sagemaker-569A31?style=flat-square&logo=amazon&logoColor=white" height="20"/></a>: Prepare, build, train, and deploy ML models<br>
<a href="https://airflow.apache.org/" target="_blank"><img alt="Apache Airflow" src="https://img.shields.io/badge/-Apache Airflow-017CEE?style=flat-square&logo=apacheairflow&logoColor=white" height="20"/></a>: Orchestrate the MLOps pipeline<br>
<a href="https://scikit-learn.org/stable/index.html" target="_blank"><img alt="Scikit-learn" src="https://img.shields.io/badge/-Sklearn-fa9c3c?style=flat-square&logo=scikitlearn&logoColor=white" height="20"/></a>: Machine Learning<br>
<a href="https://jupyter.org/" target="_blank"><img alt="Jupyter" src="https://img.shields.io/badge/-Jupyter-eb6c2d?style=flat-square&logo=jupyter&logoColor=white" height="20"/></a>: R&D<br>
<a href="https://www.python.org/" target="_blank"><img alt="Python" src="https://img.shields.io/badge/-Python-4B8BBE?style=flat-square&logo=python&logoColor=white" height="20"/></a>
<a href="https://www.anaconda.com/" target="_blank"><img alt="Anaconda" src="https://img.shields.io/badge/-Anaconda-3EB049?style=flat-square&logo=anaconda&logoColor=white" height="20"/></a>
<a href="https://code.visualstudio.com/" target="_blank"><img alt="VSC" src="https://img.shields.io/badge/-VSC-41c473?style=flat-square&logo=VisualStudioCode&logoColor=white" height="20"/></a>
<a href="https://www.docker.com/" target="_blank"><img alt="Docker" src="https://img.shields.io/badge/-Docker Compose-0db7ed?style=flat-square&logo=docker&logoColor=white" height="20"/></a>
<a href="https://git-scm.com/" target="_blank"><img alt="Git" src="https://img.shields.io/badge/-Git-F1502F?style=flat-square&logo=git&logoColor=white" height="20"/></a>

## **Ambiente Virtual**

Crear y activar ambiente virtual:

```commandline
cd 05-mlops-aws-architecture

python3.10 -m venv mlops-aws-env
source py_env/bin/activate
pip install --upgrade pip
```

Instalar las librerias necesarias para el desarrollo del proyecto, que se encuentran detalladas en el archivo `requirements.txt`:

```commandline
pip install -r requirements.txt

# Kernel
ipython kernel install --user --name=mlops-aws-env
```

## **Configuración**

Limpiar logs y crear carpeta para poder ejecutar Airflow:

```commandline
rm -r -f ./airflow/logs
mkdir -p ./airflow/logs ./airflow/plugins
```

Renombrar el archivo `.env_sample` a `.env`.

```commandline
cp .env_sample .env
. .env
```

Actualizar las siguientes variables:
   - AWS_ACCESS_KEY_ID
   - AWS_SECRET_ACCESS_KEY
   - AWS_REGION
   - AWS_BUCKET_NAME

Obtener datos de configuración en AWS:

```commandline
aws configure
```

Generar las políticas y roles para el usuario en AWS y poder utilizar los siguientes servicios:
   - S3: AmazonS3FullAccess.
   - ECR: AmazonEC2ContainerRegistryFullAccess.
   - Sagemaker: AmazonSageMakerFullAccess.

Crear bucket en S3 (de acuerdo a nombre considerado en `.env`).

Algunos comandos de AWS Cli para revisar la configuración y servicios activos:

```commandline
# Usuarios
aws iam list-users

# Políticas
aws iam list-attached-user-policies --user-name NOMBRE_USUARIO

# Roles
aws iam list-roles

# Buckets 
aws s3 ls

# Endpoints
aws sagemaker list-endpoints

# Imágenes
aws sagemaker list-images

# Modelos
aws sagemaker list-models

# Artefactos
aws sagemaker list-artifacts
```

## **Contenedores**

Ejecutar los Dockerfile que contienen la configuración de cada proceso del pipeline:

```commandline
cd dockerfiles

cd airflow
docker build -t mlops-airflow .
cd ..

cd jupyter
docker build -t mlops-airflow .
cd ..

cd mlflow
docker build -t mlops-airflow .
cd ../..

docker-compose up --build -d
```

Visualizar recursos creados:

```commandline
# Contenedores:
docker ps
docker ps -a

# Imágenes:
docker images
docker images --filter "reference=mlops-airflow"
```

### Urls

- <a href="http://localhost:8080" target="_blank">http://localhost:8080<a/> for `Airflow`. Use credentials: airflow/airflow
- <a href="http://localhost:5000" target="_blank">http://localhost:5000<a/> for `MLflow`.
- <a href="http://localhost:8893" target="_blank">http://localhost:8893<a/> for `Jupyter Lab`. Use token: mlops

### Cleanup

Detener los contenedores a través de `docker-compose`:

```commandline
docker-compose stop
```

O detener los contenedores a través de `docker`:

```commandline
docker stop $(docker ps -q)

# Eliminar contenedores
docker rm $(docker ps -aq)
```

Finalmente, eliminar los `volume`:

```commandline
docker volume rm $(docker volume ls -q)
```

## **Entrenamiento del modelo**

Ejecutar el DAG de Airflow que realiza el proceso de entrenamiento de los modelos ML.

![](images/airflow_1_panel.PNG)

## **MLflow UI**

Resultados en interfaz de MLflow.

![](images/mlflow_1_panel.PNG)

## **Deployment**

### Local

- En MLflow y AWS identificar el artefacto en producción y generar las variables necesarias para el despliegue del modelo.
   - AWS_BUCKET_NAME=""
   - EXP_ID=""
   - RUN_ID=""
   - MODEL_NAME=""
   - PORT=1234

```commandline
mlflow models serve --model-uri s3://$AWS_BUCKET_NAME/$EXP_ID/$RUN_ID/artifacts/$MODEL_NAME -p $PORT --no-conda
```

Abrir una nueva terminal y obtener las predicciones:

```commandline
cd deployments
python3 predict_local.py
```

### Cloud

- En MLflow y AWS identificar el artefacto en producción y generar las variables para el despliegue del modelo.

```commandline
export MLFLOW_TRACKING_URI=http://localhost:5000
EXP_ID=""
RUN_ID=""
MODEL_NAME=""
IMAGE_NAME=
AWS_BUCKET_NAME=""
```

- Dockerizar el artefacto (en local) apuntando a un artefacto en cloud:

```commandline
mlflow models build-docker --name $IMAGE_NAME --model-uri s3://$AWS_BUCKET_NAME/$EXP_ID/$RUN_ID/artifacts/$MODEL_NAME --env-manager conda

# Verificar la imagen creada:
docker images
```

- Cargar la imagen de Docker en AWS.

```commandline
mlflow sagemaker build-and-push-container --no-build -c $IMAGE_NAME

# Verificar los servicios creados:
aws ecr list-images --repository-name NOMBRE_IMAGEN
```

![](images/ecr_1.PNG)

- Realizar el despliegue en SageMaker:

```commandline
cd deployments
python3 deploy.py
```

Verificar los servicios creados:

```commandline
# Modelo
aws sagemaker list-models

# Endpoint
aws sagemaker list-endpoints
```

![](images/sagemaker_1_model.PNG)

![](images/sagemaker_2_endpoint.PNG)

- Obtener las predicciones:

```commandline
cd deployments
python3 predict.py
```

![](images/predictions.PNG)

## **Github**

Generar los commits del avance del proyecto:

```commandline
git init
git pull

git branch dev
git checkout dev

git add .
git commit -m "agregando proyecto 05"
git push origin dev
```

Merge con rama main:

```commandline
git checkout main
git merge dev -m "merge dev sin conflictos"
```

Link del <a href="https://github.com/alangrosso/datapath-mle/tree/main/05-mlops-aws-architecture" target="_blank">repo<a/>.
