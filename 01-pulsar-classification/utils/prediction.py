import sys
import pickle
from joblib import load
import pandas as pd
import numpy as np

SCALER_PATH = 'scaler.joblib'
MODEL_PATH = 'model.joblib'

# Load scaler
scaler = load(SCALER_PATH)

# Load model
model = load(MODEL_PATH)

# Variables 
vars_final = ['Mean_Integrated', 'SD', 'EK', 'Mean_DMSNR_Curve', 'SD_DMSNR_Curve', 'EK_DMSNR_Curve']

def get_prediction(Mean_Integrated, SD, EK, Mean_DMSNR_Curve, SD_DMSNR_Curve, EK_DMSNR_Curve):
    aux = scaler.transform(np.array([Mean_Integrated, SD, EK, 
        Mean_DMSNR_Curve, SD_DMSNR_Curve, EK_DMSNR_Curve]).reshape(1, 6))
    normalized = pd.DataFrame(aux, columns=list(vars_final))
    prediction = round(float(model.predict_proba(normalized)[:,1]),4)

    return prediction

if __name__ == "__main__":
    MEAN_INTEGRATED = 0.7439
    SD = 0.6277
    EK = 0.2066
    MEAN_DMSNR_CURVE = 0.0264
    SD_DMSNR_CURVE = 0.1152
    EK_DMSNR_CURVE = 0.4540
    prediction = get_prediction(MEAN_INTEGRATED, SD, EK, 
        MEAN_DMSNR_CURVE, SD_DMSNR_CURVE, EK_DMSNR_CURVE)
    print(f'Prediction: {prediction}')