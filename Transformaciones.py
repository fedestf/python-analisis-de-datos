import numpy as np 
#-------------------------------------------------------
arrayEnteros = np.random.randint(100,size=(4,4)) # creo una matriz aleatoria de 3x4 con valores de 0 a 100

print(arrayEnteros)

#-------------------------------------------------------
transformacion=arrayEnteros.astype(float) #transformacion a float 

print (transformacion)

#-------------------------------------------------------
arrayEnteros=arrayEnteros.reshape(4,4) #modifica las dimensiones del array

print(arrayEnteros)

#-------------------------------------------------------
arrayPlano=arrayEnteros.flatten() #crea un array unidimensional desde el original

print(arrayPlano)

#-------------------------------------------------------
listaArray=arrayPlano.tolist() #convierte el array unidimensional a una lista

print(listaArray)

#-------------------------------------------------------
arraySeparado=np.split(arrayEnteros,4)#separa el array array plano en 4 arrays 

print(arraySeparado)

arrayConcatenado=np.concatenate((arraySeparado[0],arraySeparado[3])) # concatena el array separado

print(arrayConcatenado)

#-------------------------------------------------------
arrayTranspuesto=arrayEnteros.T #creo la matriz transpuesta, las filas pasan a ser las columnas
print(arrayTranspuesto)

