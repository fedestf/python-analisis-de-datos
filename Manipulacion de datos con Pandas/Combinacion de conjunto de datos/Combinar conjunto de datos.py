import numpy as np
import pandas as pd


clima_p = pd.read_csv('ny_precipitaciones.csv')
clima_t = pd.read_csv('ny_temperaturas.csv')


# SELECCION POR FILTRADO
precip_itaca = clima_p[clima_p["NAME"] == "ITHACA CORNELL UNIVERSITY, NY US"]

# # pd.merge() de forma determinada realiza un inner join entre ambos dataframe
# # devuelve un dataframe como resultado con ambos dataframe
itaca_inner_merge = pd.merge(precip_itaca, clima_t)

# indicar que tipo de inner join hace el merge
# outer join
itaca_outer_merge = pd.merge(precip_itaca, clima_t,
                             how="left",
                             on=["STATION", "DATE"])
# left join
itaca_left_merge = pd.merge(precip_itaca, clima_t,
                            how="left",
                            on=["STATION", "DATE"])
# right join
itaca_right_merge = pd.merge(clima_t, precip_itaca,
                             how="right",
                             on=["STATION", "DATE"])

# metodo join() nos permite combinar datos

clima_join = clima_t.join(clima_p, lsuffix='_left')

clima_p.set_index(["STATION", "DATE"])

clima_joined_total = clima_t.join(clima_p.set_index(["STATION", "DATE"]),
                                  lsuffix="_X",
                                  rsuffix="_Y",
                                  on=["STATION", "DATE"]
                                  )

for i in clima_joined_total.columns:
    print(i)

# pd.concat() nos permite hacer concatenaciones de dataframes a traves de un eje,fila o columnas

clima_total_outer_concat = pd.concat(
    [clima_t, clima_p], axis=1)  # clima p en clima t

clima_total_outer_concat = pd.concat(
    [clima_t, clima_p], axis=0)  # clima t en clima p


df_jerar = pd.concat([clima_t, clima_p],
                     keys=["temp", "precip"])  # primer clave al primer dataframe,segunda clave al segundo dataframe

print(df_jerar)
