import numpy as np
import pandas as pd

# Función para visualizar percentiles
def cuantiles(lista):
    c = [0,1,5,10,20,25,30,40,50,60,70,75,80,90,92.5,95,97.5,99,100]
    matrix = pd.concat([pd.DataFrame(c),pd.DataFrame(np.percentile(lista.dropna(),c))],axis = 1)
    matrix.columns = ["Cuantil", "Valor_Cuantil"]
    return(matrix)