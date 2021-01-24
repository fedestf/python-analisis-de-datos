import numpy as np

# creo un array de 8x8 que va de 0 a 63
arrayTest = np.array(range(64)).reshape((8, 8))

print(arrayTest[1, 1])  # posicion 1,1
# desde la fila 0 hasta la fila 7 y que la seleccione de 2 en 2 tomando los 4 primeros elementos
print(arrayTest[0:7:2, 4])
# trae los elementos a partir de la posicion 3 hasta el final , poniendole los : y una cota superior cuenta hasta ese numero
print(arrayTest[1, 3:5])
# uso el indice de la izquierda y lo junto con el de la derecha y los cruzo para saber la coordenada y el valor contenido en la matriz
print(arrayTest[[1, 3, 5], [3, 6, 7]])
# accede a las filas 1,3,5 y trae todos los numeros contando de 3 en 3
print(arrayTest[[1, 3, 5], ::3])

# ---------------------------------------------------------------------------------------------- indexacion booleana

data = np.arange(8)

print(data < 4)  # revisa todas las posiciones del array y revisa si son menores a 4 y devuelve true or false dependiendo de los valores del array
print(data[data < 4])  # me imprime todos los valores del array que sean true

amigos = np.array(['giulia', 'victor', 'joel', 'andrea',
                   'valentina', 'albert', 'roque'])

print('giulia' in amigos)  # pregunto si giulia esta en el array amigos

# devuelve todos los valores del array que sean distintos que giulia
print(amigos[amigos != 'giulia'])
