import sys
import pickle
from joblib import load
import pandas as pd
import numpy as np

import warnings
warnings.filterwarnings('ignore')

from utils.prediction import get_prediction

vars_final = ['Mean_Integrated', 'SD', 'EK', 'Mean_DMSNR_Curve', 'SD_DMSNR_Curve', 'EK_DMSNR_Curve']

# Evaluar argumentos de entrada por consolta y obtener predicción
if len(sys.argv)==7: # main.py + 6 variables de entrada
    # valores de las variables
    arguments = sys.argv[1:]
    # Asignar variable y valor
    for i in range(len(vars_final)):
        if i <= len(arguments):
            locals()[vars_final[i]] = arguments[i]
    # Comprobar las asignaciones
    for var in vars_final:
        print(var + ' = ' + str(eval(var)))
    # Prediction    
    prediction = get_prediction(arguments[0], arguments[1], arguments[2],
        arguments[3], arguments[4], arguments[5])
    print(f'Prediction: {prediction}')
else:
    print('0 or more arguments received')


    