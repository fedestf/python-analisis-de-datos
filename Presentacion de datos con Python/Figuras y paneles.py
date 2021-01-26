import numpy as np
import matplotlib.pyplot as plt

fig, panel = plt.subplots()

x = np.linspace(0, 4*np.pi, 100)
y = np.sin(x)

panel.plot(x, y)


# crear una figura con 2 paneles horizontales

fig2, (pan_1, pan_2) = plt.subplots(2, 1)
# figura 1
x1 = np.linspace(0, 4*np.pi, 100)
y1 = np.sin(x1)
pan_1.plot(x1, y1)

# figura 2
x2 = np.linspace(0, 4*np.pi, 100)
y2 = np.sin(x2)
pan_2.plot(x2, y2)

# Guardar figura
plt.savefig('grafico_test.png')

# Crear una figura con 2 paneles verticales

# constrained_layout sirve para separar los graficos
fig2, (pan_1, pan_2) = plt.subplots(1, 2, constrained_layout=True)
# figura 1
x1 = np.linspace(0, 4*np.pi, 100)
y1 = np.sin(x1)
pan_1.plot(x1, y1)

# figura 2
x2 = np.linspace(0, 4*np.pi, 100)
y2 = np.sin(x2)
pan_2.plot(x2, y2)

# Crear mas de 2 graficos

fig3, ((pan_1, pan_2), (pan_3, pan_4)) = plt.subplots(
    2, 2, constrained_layout=True)
# figura 1
x1 = np.linspace(0, 4*np.pi, 100)
y1 = np.sin(x1)

pan_1.plot(x, y)
pan_2.plot(x, y**2)
pan_3.plot(x, -y)
pan_4.plot(x, -y**2)

for ax in fig3.get_axes():
    ax.set(xlabel='x-label', ylabel='y-label')  # Etiequetar los ejes con X e Y

# paneles que comparten eje x o y dependiendo si usamos sharex o sharey

fig4, (pan_1, pan_2) = plt.subplots(2, sharex=True)

x = np.linspace(0, 4*np.pi, 100)
y = np.sin(x1)

pan_1.plot(x, y, 'tab:orange')  # con 'tab:color' cambio de color los graficos
pan_2.plot(x+1, -y, 'green')

fig5, paneles = plt.subplots(2, 2, sharex='col', sharey='row')

(pan_1, pan_2), (pan_3, pan_4) = paneles

pan_1.plot(x, y)
pan_2.plot(x, y**2, 'tab:orange')
pan_3.plot(x + 1, -y, 'tab:green')
pan_4.plot(x + 2, -y ** 2, 'tab:red')

# Metodo .twinx() sirve para graficar ambas funciones en un mismo panel

fig6, pan_1 = plt.subplots(1, 1)
pan_2 = pan_1.twinx()

x1 = np.linspace(0, 4*np.pi, 100)
y1 = np.sin(x1)

pan_1.plot(x1, y1, 'b')  # si pongo 'o' hace puntos donde esta la funcion

x2 = np.linspace(0, 4*np.pi, 100)
y2 = np.cos(x2)

pan_2.plot(x2, y2, 'r')  # otra forma de pasar el color

plt.show()  # funcion para mostrar el grafico
