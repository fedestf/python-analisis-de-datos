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

x = [1, 2, 3, 4, 5]
y = [1, 1, 2, 3, 5]
y2 = [0, 4, 2, 6, 8]
y3 = [1, 3, 5, 7, 9]

etiquetas = ['Sector privado', 'Sector publico', 'Sector informal']

fig, panel = plt.subplots()

panel.stackplot(x, y, y2, y3,
                labels=etiquetas,
                colors=['r', 'w', 'b'])

panel.legend(loc='upper left')
panel.set_title("Grafico apilado")
plt.show()

# Graficos de tortas

etiquetas = ['Financiera', 'Salud', 'Construccion']
sectores = [56, 66, 24]
colores = ['c', 'g', 'r']

plt.pie(sectores, labels=etiquetas, colors=colores,
        startangle=90,  # angulo en el que arranca el grafico
        explode=(0, 0, 0),  # Valores de cuanto quiero separar las partes
        autopct='%1.2f',
        shadow=True)  # cuandos decimales tienen los valores
plt.axis('equal')  # partes iguales desde los ejes
plt.title('Ejemplo de grafico torta')
plt.show()

# Grafico BoxPlot

y1 = np.random.normal(100, 10, 100)
y2 = np.random.normal(80, 30, 100)
y3 = np.random.normal(90, 20, 100)
y4 = np.random.normal(70, 25, 100)

datos = [y1, y2, y3, y4]
fig, panel = plt.subplots()

panel.set_xticklabels(['Grupo_1', 'Grupo_2', 'Grupo_3', 'Grupo_4'])
bp = panel.boxplot(datos, patch_artist=True)
plt.title('Ejemplo de BoxPlot')
# Elementos del BoxPlot
for box in bp['boxes']:
    box.set(color='r', linewidth=2)
    box.set(facecolor='b')

for whisker in bp['whiskers']:  # modifica los bigotes
    whisker.set(color='g', linewidth=2)

for cap in bp['caps']:
    cap.set(color='black', linewidth=3)

for median in bp['medians']:
    median.set(color='#b2df8a', linewidth=2)

for flier in bp['fliers']:
    flier.set(marker='*', color='r', alpha=1)

plt.show()
