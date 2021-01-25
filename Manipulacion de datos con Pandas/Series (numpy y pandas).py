import numpy as np
import pandas as pd

# crear una serie con indices automaticos
serie = pd.Series([1979, 1980, 1981, 1982])

print(serie)
print(serie.values)  # veo los valores de la serie
# veo los indices de la serie RangeIndex(start=0, stop=4, step=1)
print(serie.index)

# Definir el indice manualmente y pasarlo como argumento

serieTest = pd.Series([1989, 1990, 1991, 1992, 1993], index=[
                      'daniela', 'valentina', 'andrea', 'sherazade', 'genesis'])
print(serieTest)

# Crear series a partir de diccionarios,arrays,etc

# serie creada a partir del modulo rand
serieTest2 = pd.Series(np.random.rand(10))
print(serieTest2)

# diccionario creado a partir de un for
diccionario = {'cuadrado de {}'.format(i): i*i for i in range(11)}
print(diccionario)

# serie creada a partir de un diccionario
serieDiccionario = pd.Series(diccionario)
print(serieDiccionario)
