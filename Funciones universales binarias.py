import numpy as np

a = np.array([5, 36, 17, 18, 9])
b = np.array([8, 24, 17, 19, 9])

print(np.add(a, b))  # suma de array
print(np.subtract(a, b))  # resta de array
print(np.multiply(a, b))  # multiplicacion de array
print(np.divide(a, b))  # division de array
print(np.array_equal(a, b))  # pregunta si es igual de array a array
# nos devuelve un array con los valores minimos de los 2 array por posicion
print(np.fmin(a, b))
print(np.fmax(a, b))  # devuelve los valores maximos de cada array por posicion
