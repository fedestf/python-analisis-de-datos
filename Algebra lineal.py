import numpy as np

print("\n ------------------")  # PRODUCTO DE ARRAYS
a = np.array([1, 2, 3], float)
b = np.array([0, 1, 1], float)

print(np.dot(b, a))

print("\n ------------------")  # PRODUCTO DE MATRICES

a1 = np.array([[5, 2], [4, 8]], float)
b1 = np.array([[2, 4], [5, 3]], float)

print(a1, "\n ------------------")
print(b1, "\n ------------------")

print(a1@b1)  # multiplicador de matrices

print("\n ------------------")  # ARRAY N DIMENSIONAL

a2 = np.array([[0, 1, 4], [5, 2, 3], [1, 4, 8]], float)
b2 = np.array([2, 3, 5], float)

print(a2, "\n ------------------")
print(b2, "\n ------------------")

print(b2@a2)

print("\n ------------------")  # DETERMINANTE DE UNA MATRIZ

a3 = np.array([[8, 5], [3, 4]])
print(a3, "\n --------")

print(np.linalg.det(a3))

print("\n ------------------")  # AUTO VALORES Y AUTO VECTORES

vals, vecs = np.linalg.eig(a3)
print(vals, "\n ------------------")
print(vecs, "\n ------------------")
