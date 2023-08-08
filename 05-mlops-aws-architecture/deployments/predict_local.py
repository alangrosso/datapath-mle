import requests
import pandas as pd

url = "http://127.0.0.1:1234/invocations"

# Import data
data = pd.read_csv("../data/output_data/x_test.csv")
print('Total Rows:', len(data))

# Prepare data
input_data = data[:10].values.tolist()
body = {"inputs": input_data}
headers={ 'ContentType':'application/json'}

# Send data via url
response = requests.post(url, headers=headers, json=body)

# Manejar la respuesta del modelo
if response.status_code == 200:
    result = response.json()
    print("Respuesta del modelo:", result)
else:
    print("Error al realizar la consulta:", response.text)

