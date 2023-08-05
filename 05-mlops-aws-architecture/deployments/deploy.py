# DEPLOYMENT
# https://mlflow.org/docs/latest/python_api/mlflow.sagemaker.html

from mlflow.deployments import get_deploy_client

# Configuración de AWS
region = 'us-west-1' # actualizar
aws_id = '774809889886' # actualizar
bucket = 'mlops-bucket-agr' # actualizar
role_arn = 'arn:aws:iam::774809889886:role/aws-sagemaker-for-deploy-ml-model' # actualizar

# URI del modelo en MLflow
mlflow_experiment_id = '3' # actualizar
mlflow_run_id = '' # actualizar de acuerdo a run id
model_name = 'production_model' # actualizar con nombre tipo de modelo
model_uri = f's3://{bucket}/{mlflow_experiment_id}/{mlflow_run_id}/artifacts/{model_name}' # ruta del mismo modelo que fue dockerizado
# model_uri = f'models:/{model_name}/Production' # ruta del mismo modelo que fue dockerizado

# Deployment
image_name = 'mlops-image-agr'
deployment_name = 'mlops-deploy-agr'
tag_id = '2.2.0'
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
