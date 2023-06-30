from fastapi import APIRouter, HTTPException, status
from models.models import Prediction_Input, Prediction_Output

from joblib import load
import pandas as pd
import numpy as np

# Variables 
vars_final = ['Mean_Integrated', 'SD', 'EK', 'Mean_DMSNR_Curve', 'SD_DMSNR_Curve', 'EK_DMSNR_Curve']

# Artefactos
SCALER_PATH = 'artifacts/scaler.joblib'
MODEL_PATH = 'artifacts/model.joblib'
# Scaler
scaler = load(SCALER_PATH)
# Modelo ML
model = load(MODEL_PATH)

router = APIRouter()

preds = []

@router.get("/ml")
def get_preds():
    return preds

@router.post('/ml', status_code=status.HTTP_201_CREATED)
def get_prediction(pred_input: Prediction_Input):
    input_values = [pred_input.Mean_Integrated, pred_input.SD, 
        pred_input.EK, pred_input.Mean_DMSNR_Curve, 
        pred_input.SD_DMSNR_Curve, pred_input.EK_DMSNR_Curve]
    input_array = np.array(input_values).reshape(1, 6)
    input_scaled = scaler.transform(input_array)
    normalized = pd.DataFrame(input_scaled, columns=list(vars_final))
    prediction = round(float(model.predict_proba(normalized)[:,1]),4)
    prediction_dict = {
        'id': pred_input.id, # str(pred_input.id), 
        'prediction': float(prediction)
        }
    preds.append(prediction_dict)
    return {"message": "Creado satisfactoriamente"}

@router.put('/ml/{pred_id}')
def update_prediction(pred_id: int, pred_out: Prediction_Output):
    for pred in preds:
        if pred["id"] == pred_id:
            pred.update(pred_out.dict())
            return pred
    raise HTTPException(status_code=404, detail='Not found')

@router.delete('/ml/{pred_id}')
def delete_prediction(pred_id: int):
    for pred in preds:
        if pred["id"] == pred_id:
            preds.remove(pred)
            return {"message": "Borrado satisfactoriamente"}
    raise HTTPException(status_code=404, detail='Not found')