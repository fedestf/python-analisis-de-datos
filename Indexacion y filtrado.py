import numpy as np
import pandas as pd

df = pd.DataFrame(
                    np.random.randint(low=0,high=10,size=(10,2)), #valores aleatorios de 0 a 10 con tamaño de 10 columnas y 2 filas
                    index=['a','b','c','d','e','f','g','h','i','j'],
                    columns=["Cod_empleado","Calificacion"]
                 )

#loc es la abreviacion de location

print(df.loc['a']) #pasamos el nombre del indice que queremos seleccionar
print(df.loc['b':'f'])#pasamos el rango de valores que queremos traer
print(df.loc[df.index[3:7],'Cod_empleado'])#pasamos la columna en especial que queremos traer los valores con el rango de indices que queremos 

#iloc abreviacoin de index location
print(df.iloc[0:3])#filas de indice 0 hasta indice 3
print(df.iloc[3:])#filas de indice 3 hasta el final

