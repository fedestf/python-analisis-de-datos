import numpy as np
import pandas as pd

data = {
    'pais': ['Caracas', 'Guadalajara', 'La habana', 'Cancun', 'Guasdalito'],
    'poblacion': [100000, 200000, 340000, 210000, 300000],
    'casos': [6000, 4000, 35000, 4300, 3002]
}

df = pd.DataFrame(data)  # creo el dataframe a partir de la info ingresada
print(df)
