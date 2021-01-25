import numpy as np
import pandas as pd

ratings = pd.read_csv('ratings.csv')
peliculas = pd.read_csv('peliculas.csv')
usuarios = pd.read_csv('usuarios.csv')

# un rating requiere un usuario y una pelicula
# los dataframes estan vinculaods por una clave(user_id,peli_id)

# es posible que un usuario este asociado a 0-N ratings y peliculas,
# de la misma forma una pelicula puede tener 0-N ratings por N usuarios

peli_ratings = pd.merge(peliculas, ratings)
clasif = pd.merge(peli_ratings, usuarios)

# 10 peliculas con mas rating
mas_rating = clasif.groupby('titulo').size().sort_values(
    ascending=False)[0:10]  # cotas de 0 a 10 en peliculas

# metodo .agg() nos permite aplicar una lista de funciones en columnas especificas
# si queremos saber el rating promedio de cada pelicula

peli_stats = clasif.groupby('titulo').agg({'rating': [np.size, np.mean]})

print(peli_stats.sort_values([('rating', 'mean')], ascending=False).head())

# peliculas con minimo de 100 reviews
conMasDe100Reviews = peli_stats['rating']['size'] >= 100

print(peli_stats[conMasDe100Reviews].sort_values(  # ordeno por clasificacion y promedio
    [('rating', 'mean')], ascending=False)[0:10])  # ordeno que me muestre las primeras 10 peliculas
