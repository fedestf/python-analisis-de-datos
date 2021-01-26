import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df_crudo = pd.read_csv('dow_jones_index.data')

# seleccionamos los datos que vamos a usar
columnas = ['accion', 'fecha', 'precio']
df = pd.read_csv('dow_jones_index.data',
                 usecols=[1, 2, 5],
                 header=0,
                 names=columnas,
                 parse_dates=['fecha'],
                 converters={'precio':
                             lambda x:
                             float(x.replace('$', ''))
                             }
                 )
print(df)

# Periodo de tiempo que representan los datos
print('Pertenecen al año :', df.fecha.dt.year.value_counts())

# Saber que meses aparecen
print('Los meses que aparece son\n', df.fecha.dt.month_name().value_counts())

# Saber por qué hay 30 registros mas en abril que en los meses restantes
df['mes'] = df.fecha.dt.month_name()
filtro1 = df['mes'] == 'April'
filtro2 = df['mes'] == 'May'

# Muestra que en abril tuvieron 5 registros
df[filtro1].groupby('accion')['mes'].value_counts()
# muestra que en los demas meses tuvieron 4
df[filtro2].groupby('accion')['mes'].value_counts()

# Que acciones en promedio tuvieron la mayor y la menor cotizacion ordenada de mayor a menor
print(df.groupby('accion').agg({'precio': [np.mean, np.std]}).sort_values(
    [('precio', 'mean')], ascending=False))

# Mayor y menor variacion de precio
print(df.groupby('accion').agg({'precio': [np.mean, np.std]}).sort_values(
    [('precio', 'std')], ascending=False))

# Creamos un nuevo dataframe para analisar acciones en particulares

df_nuevo = df.pivot_table(index='fecha',
                          columns='accion',
                          values='precio')

# Ahora se pueden comenzar a crear graficos para analizar la informacion
fig, (pan1, pan2) = plt.subplots(2, 1, sharex=True, constrained_layout=True)

# PANEL DE LA ACCION CAT
pan1.plot(df_nuevo.index, df_nuevo.CAT,
          color='blue',
          marker='o',
          linestyle='solid',
          label='CAT')

# PANEL DE LA ACCION AA
pan2.plot(df_nuevo.index, df_nuevo.AA,
          color='orange',
          marker='v',
          linestyle='solid',
          label='AA')

# PARA CADA X DE LOS PANELES VA A INGRESAR LOS DATOS DESCRIPTIVOS
for pan in fig.get_axes():
    pan.set(xlabel='fecha',
            ylabel='Dolares americanos',
            title='Precio de la accion al cierre')

pan1.legend()
pan2.legend()
plt.savefig('Grafico 1 Acciones CAT y AA.png')

# existe alguna correlacion entre los precios de cat y el resto de las acciones?
# correlaciones respecto de cat a las demas acciones
# Traigo todas las correlaciones mayores a 0.8
corr_pos = df_nuevo.corr().loc['CAT'][df_nuevo.corr(
).loc['CAT'] > 0.8].sort_values(ascending=False)

valores = corr_pos[1:5]
plt.bar(valores.index, valores.values, color='green')
plt.plot()
plt.xlabel('Acciones')
plt.ylabel('Coeficiente de correlacion')
plt.title('Correlacion entre CAT y el resto')
plt.show()
