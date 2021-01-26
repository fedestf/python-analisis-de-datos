import numpy as np
import matplotlib.pyplot as plt

fig, pan_1 = plt.subplots(1, 1)

x1 = np.linspace(0, 4*np.pi, 100)
y1 = np.sin(x1)

pan_1.plot(x1, y1, label='Seno')  # describo el trazado como seno
pan_1.legend(loc='best')  # coloca la leyenda seno en la mejor posicion posible

fig, pan_1 = plt.subplots(1, 1)
pan_2 = pan_1.twinx()
x1 = np.linspace(0, 4*np.pi, 100)
y1 = np.sin(x1)

funcion1 = pan_1.plot(x1, y1, color='b', marker='^',
                      markeredgecolor='b', markerfacecolor='g', label='Seno')

x2 = np.linspace(0, 4*np.pi, 100)
y2 = np.cos(x2)

funcion2 = pan_2.plot(x2, y2, color='r', marker='o',
                      markeredgecolor='r', markerfacecolor='y', label='Coseno')

funciones = funcion1+funcion2  # contengo ambos graficos en una variable

# hago una lista con los valores de label de cada funcion
labels = [f.get_label() for f in funciones]

plt.legend(funciones, labels, loc='best')

# etiquetas de eje
pan_1.set_xlabel('$Eje x$')  # poniendo $ antes y despues, se pone en italica
pan_1.set_ylabel('$Eje y_1$')
pan_2.set_ylabel('$Eje y_2$')

# poner titulo al grafico
plt.title('Seno y coseno')

# plt.tight_layout()  # comprime el espacio de la figura para hacer el grafico mas chico

plt.show()
