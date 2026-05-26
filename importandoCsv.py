import pandas as pd

df=pd.read_csv("Vote_Ai.csv")

# Imprime si lee el archivo
print("OKEY! Archivo cargado correctamente")

# Mostrando las primeras filas del dataframe
print(df.head())

# Filtrando por año 2022
#resultado = df[df['year'] == 2022]
#resultado = df[df['State'] == 'Bihar']

#resultado = df['Election_ID'].count()
resultado = df['Election_ID'].sum()

# Mostrando resultado
print(resultado)

filtro_avanzado = df["State"].str.startswith('Ba', na =False)
df_filtrado = df[filtro_avanzado]
