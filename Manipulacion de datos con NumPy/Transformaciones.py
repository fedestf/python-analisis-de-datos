import numpy as np
# -------------------------------------------------------
# creo una matriz aleatoria de 3x4 con valores de 0 a 100
arrayEnteros = np.random.randint(100, size=(4, 4))

print(arrayEnteros)

# -------------------------------------------------------
transformacion = arrayEnteros.astype(float)  # transformacion a float

print(transformacion)

# -------------------------------------------------------
arrayEnteros = arrayEnteros.reshape(4, 4)  # modifica las dimensiones del array

print(arrayEnteros)

# -------------------------------------------------------
# crea un array unidimensional desde el original
arrayPlano = arrayEnteros.flatten()

print(arrayPlano)

# -------------------------------------------------------
listaArray = arrayPlano.tolist()  # convierte el array unidimensional a una lista

print(listaArray)

# -------------------------------------------------------
# separa el array array plano en 4 arrays
arraySeparado = np.split(arrayEnteros, 4)

print(arraySeparado)

arrayConcatenado = np.concatenate(
    (arraySeparado[0], arraySeparado[3]))  # concatena el array separado

print(arrayConcatenado)

# -------------------------------------------------------
# creo la matriz transpuesta, las filas pasan a ser las columnas
arrayTranspuesto = arrayEnteros.T
print(arrayTranspuesto)
