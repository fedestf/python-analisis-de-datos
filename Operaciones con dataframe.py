import numpy as np
import pandas as pd

array = [np.random.randint(50,size=(10))]

df=pd.DataFrame(array).T #transpuesta de dataframe para que sea una sola columna

# agregar nuevas columnas al dataframe
df['experiencia']=5
df['perdidas']= [(i+2)*np.e for i in range (10)]
df['columna exp x2'] = df['experiencia']*2

#modificar nombre de las columnas del dataframe
df.columns= ['codigo_id','años_exp','indice','eficiencia']

#modificar una sola columna
df['indice']=df['indice']/200 #divido todos los valores de indice por 200

#eliminar una columna
del df['eficiencia']

#modificar el indice del data frame
i=['a','b','c','d','e','f','g','h','i','j']
df.index=i

#como todo lo de pandas incluye numpy se puede utilizar los metodos de matematica aprendidos antes , dejo un par como ej

print(df['años_exp'].sum()) #sumo todos los valores de la columna de añox_exp
print(df['codigo_id'].min()) #busco el minimo en la columna de codigo_id
print(df['codigo_id'].max()) #busco el maximo en la columna de codigo_id

print(df)

#borra las filas a,e,d del dataframe con el metodo drop
c=df.drop(['a','e','d'],axis=0)

print (c)




