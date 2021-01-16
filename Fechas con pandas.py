import numpy as np
import pandas as pd
import datetime
from datetime import timedelta

#metodo to_datetime()

fecha = pd.to_datetime('24th April, 2020')
print(fecha)

#metodo to_timedelta() nos permite calcular dias antes o despues de una fecha determinada

fecha2 = fecha + pd.to_timedelta(4,unit='D') #sumo 4 dias a la fecha generada anteriormente
print(fecha2)

#metodo date_range() permite generar un rango de fechas

fechas_inicio = pd.date_range(start='24/4/2020',end='24/5/2020',freq='D')
fechas_fin = pd.date_range(start='24/5/2020',end='24/6/2020',freq='D')

lista_equis = []

for i in range(15):
    lista_equis.append(np.random.randint(2))
    pass

df=pd.DataFrame()#creo data frame

df['Inicio_campaña']=fechas_inicio[:15]
df['Fin_campaña']=fechas_fin[:15]
df['Target']=lista_equis

#agrego columnas para expandir el analisis
df['Dia de inicio'] = df['Inicio_campaña'].dt.day
df['Mes de inicio'] = df['Inicio_campaña'].dt.month
df['Año de inicio'] = df['Inicio_campaña'].dt.year
df['Dia de inicio'] = df['Inicio_campaña'].dt.weekday
df['Semana del año de inicio'] = df['Inicio_campaña'].dt.week
df['Duracion'] = df['Fin_campaña'] - df['Inicio_campaña']
df['Dias de duracion'] = df['Duracion']/timedelta(days=1)
df['Minutos de duracion'] = df['Duracion']/timedelta(minutes=1)
df['Segundos de duracion'] = df['Duracion']/timedelta(seconds=1)
print(df)