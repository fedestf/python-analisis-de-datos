import numpy as np
import pandas as pd

serie = pd.Series([1979,1980,1981,1982]) #crear una serie con indices automaticos

print(serie)
print(serie.values)#veo los valores de la serie
print(serie.index)#veo los indices de la serie RangeIndex(start=0, stop=4, step=1)

#Definir el indice manualmente y pasarlo como argumento

serieTest=pd.Series([1989,1990,1991,1992,1993], index=['daniela','valentina','andrea','sherazade','genesis'])
print(serieTest)

#Crear series a partir de diccionarios,arrays,etc

serieTest2 = pd.Series(np.random.rand(10)) #serie creada a partir del modulo rand
print(serieTest2)

diccionario = {'cuadrado de {}'.format(i) : i*i for i in range(11)} #diccionario creado a partir de un for
print (diccionario)

serieDiccionario=pd.Series(diccionario) #serie creada a partir de un diccionario
print(serieDiccionario)