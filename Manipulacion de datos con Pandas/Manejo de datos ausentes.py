import numpy as np
import pandas as pd

df = pd.DataFrame({

    'VarA': ['aa', None, 'cc'],
    'VarB': [20, 30, None],
    'VarC': [1234, 3456, 6789]
},
    index=['Caso 1', 'Caso 2', 'Caso 3']
)

print(df)

print(pd.isnull(df))  # veo cuales son los valores null de mi dataframe
# elimino las filas con valores nulos
print(df.dropna(subset=["VarA", 'VarB']))
# funcion para llenar nulos con un espacio vacio o con un valor
print(df.fillna(""))
print(df.fillna(25))
