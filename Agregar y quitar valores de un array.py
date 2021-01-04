import numpy as np

a=np.arange(0,20,2) ##creacion de array desde 0 hasta 20 con paso 2
print(a)

array_flot=np.random.rand(4,3) #FILAS,COLUMNAS con float
print(array_flot)

array_int=np.random.randint(10,size=(2,3)) # rango de valores,size=FILAS,COLUMNAS 
print(array_int)

array_6=np.full((3,3),6) ## (FILA,COLUMNA), valor que rellena todo un array del mismo valor
print(array_6)

b=np.append(a, [1,2,3,4]) ##agrego nuevos valores al final del array A
print(b)

c=np.insert(a,2,[69,42]) ##agrego nuevos valores en determinada posicion
print (c)

d=np.delete(array_6,2,axis=1) ##eje 0 horizontal eje 1 vertical
print(d)