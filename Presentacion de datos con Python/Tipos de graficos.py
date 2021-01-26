import numpy as np
import matplotlib.pyplot as plt

# Grafico de lineas

año = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
PIB = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

plt.plot(año, PIB, color='green', marker='o', linestyle='solid')
plt.title('PIB Nominal')
plt.ylabel('Millones de $')
plt.xlabel('Año')
plt.show()

# Scatter plot

x1 = [3, 5, 7]
y1 = [3, 5, 9]

x2 = [1, 2, 3, 4]
y2 = [2, 3, 2, 3]

x3 = [8, 7, 2, 5, 4]
y3 = [6, 8, 7, 8, 7]

plt.scatter(x1, y1)
plt.scatter(x2, y2, marker='v', color='r')
plt.scatter(x3, y3, marker='^', color='m')
plt.title('Ejemplo de scatter')
plt.show()

# Grafico de barras

x = [1, 3, 4, 5, 6, 7, 8, 9]
y = [4, 7, 2, 4, 5, 8, 7, 3]

x1 = [8, 7, 2, 5, 4]
y1 = [6, 8, 7, 2, 7]

plt.bar(x, y, label='Barra azul', color='b')
plt.bar(x1, y1, label='Barra verde', color='g')
plt.xlabel('N° barras')
plt.ylabel('Altura de barras')
plt.title('Ejemplo grafico de barras')
plt.legend()
plt.show()

# Histogramas,grafican frecuencias

y = 5 + np.random.randn(100)
x = [e for e in range(len(y))]
plt.hist(y, bins=20)
plt.title('Histograma')
plt.show()

# Histogramas acumulativo

y = 5 + np.random.randn(100)
x = [e for e in range(len(y))]
plt.hist(y, cumulative=True, bins=20)
plt.title('Histograma acumulativo')
plt.show()

# Graficos apilados
