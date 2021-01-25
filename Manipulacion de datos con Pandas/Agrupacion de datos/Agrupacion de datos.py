import numpy as np
import pandas as pd

data = pd.read_csv('data_celular.csv',
                   header=0,
                   index_col=0,
                   names=['indice', 'fecha', 'duracion',
                          'item', 'mes', 'red', 'tipo_red'],
                   parse_dates=['fecha'])

# Saber cuantas filas tiene el dataframe
print("el dataframe tiene la siguiente cantidad de filas : ",
      data['item'].count())

# Total de llamadas en segundos
print("el tiempo de llamadas en segundos es : ",
      data['duracion'][data['item'] == 'call'].sum())

# redes telefonicas unicas
print("total de redes unicas", data['red'].nunique())

# metodo groupby()

print(data.groupby('mes').sum())  # duracion de llamada por mes

print("En el siguiente cuadro vemos la cantidad de entradas por mes \n en llamadas,sms y datos : \n \n",
      data.groupby(['mes', 'item'])['duracion'].count())  # cuento la cantidad de datos

print("La duracion total de las llamadas de cada operadora es :\n ",
      data[data['item'] == 'call'].groupby('red')['duracion'].sum())  # agrupo por red que es el operador y sumo las duraciones

print("llamadas,sms y datos enviados a cada operadora por mes : \n ",
      data.groupby(['mes', 'tipo_red'])['fecha'].count())  # agrupa por mes y tipo de red y cuenta las cantidades por fecha
