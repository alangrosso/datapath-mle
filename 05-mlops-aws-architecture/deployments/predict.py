import boto3
import json
import pandas as pd
 
region = '' # actualizar
endpoint_name = '' # actualizar

# Connection
runtime = boto3.Session().client(
    'sagemaker-runtime', 
    region_name=region)
 
# Import data
data = pd.read_csv("../data/output_data/x_test.csv")

# Prepare data
input_data = data[:10].values.tolist()
payload = json.dumps({"inputs": input_data}) # serializamos

# Send data via InvokeEndpoint API
response = runtime.invoke_endpoint(
    EndpointName=endpoint_name, 
    ContentType='application/json', 
    Body=payload)

# Unpack response
result = json.loads(response['Body'].read().decode())
print(result)