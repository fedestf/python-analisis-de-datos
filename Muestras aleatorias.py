import numpy as np
import pandas as pd


def crearDataSet(Number=1):
    Output = []

    for i in range(Number):
        # Crear un rango de fechas semanal (de lunes a lunes)
        rng = pd.date_range(start='1/1/2016', end='12/31/2016', freq='W-MON')
        # crear valores aleatorios
        data = np.random.randint(low=25, high=1000, size=len(rng))
        # Status posibles
        status = [1, 2, 3]
        # Lista de status aleatorios
        random_status = [status[np.random.randint(
            low=0, high=len(status))] for i in range(len(rng))]
        # states posibles
        states = ['Libertador', 'El Hatillo',
                  'El hatillo', 'Chacao', 'Baruta', 'Sucre']
        # Crear una lista aleatoria de estatuses
        random_states = [states[np.random.randint(
            low=0, high=len(states))]for i in range(len(rng))]
        Output.extend(zip(random_states, random_status, data, rng))

    return Output


dataset = crearDataSet(4)

df = pd.DataFrame(data=dataset,
                  columns=['Local', 'Estatus_local', 'cantidad_Clientes', 'Fecha_status'])

print(df)

# Funcion np.random.choice() extrae una muestra aleatoria a partir de un array unidimensional
filas = np.random.choice(df.index, 10)
print(filas)
# con df.loc muestro el dataframe creado a partir de las filas aleatorias
print(df.loc[filas])
