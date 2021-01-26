import numpy as np
import matplotlib.pyplot as plt

fig, pan_1 = plt.subplots(1, 1)

x1 = np.linspace(0, 4 * np.pi, 100)
y1 = np.sin(x1)

# configurar grafico visualmente
# linestyle tipo de linea
# color de la linea
# marcador como voy a marcar los puntos de datos
pan_1.plot(x1, y1, linestyle='--', color='g', marker='o')

# markeredgecolor color del borde del marcador
# markerfacecolor color del relleno del marcador
pan_1.plot(x1, y1, linestyle='--', color='y', marker='o',
           markeredgecolor='y', markerfacecolor='r')


plt.show()
