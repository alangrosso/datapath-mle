# DEPLOYMENT
# https://mlflow.org/docs/latest/python_api/mlflow.sagemaker.html

from mlflow.deployments import get_deploy_client

# Configuración de AWS
region = '' # actualizar
aws_id = '' # actualizar
bucket = '' # actualizar
role_arn = '' # actualizar

# URI del modelo en MLflow
mlflow_experiment_id = '' # actualizar
mlflow_run_id = '' # actualizar de acuerdo a run id
model_name = '' # actualizar con nombre tipo de modelo
# S3: ruta del mismo modelo que fue dockerizado
model_uri = f's3://{bucket}/{mlflow_experiment_id}/{mlflow_run_id}/artifacts/{model_name}' 
# Local: ruta del mismo modelo que fue dockerizado
# model_uri = f'models:/{model_name}/Production'

# Deployment
image_name = '' # imagen origen, actualizar
deployment_name = '' # destino, actualizar
tag_id = '' # versión de imagen origen, actualizar
image_url = f'{aws_id}.dkr.ecr.{region}.amazonaws.com/{image_name}:{tag_id}'

# Archivo de configuracion
config = dict(
    assume_role_arn=role_arn, execution_role_arn=role_arn, bucket=bucket, 
    image_url=image_url, region_name=region, archive=False,
    instance_count=1, synchronous=True, timeout_seconds=300
)

# Llamar servicio
client = get_deploy_client(f"sagemaker:{region}")
client.create_deployment(
    deployment_name,
    model_uri=model_uri,
    flavor="python_function", # servicio es función de tipo python
    config=config,
)
