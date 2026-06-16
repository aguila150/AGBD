import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 


# Imprime si lee el archivo
#print("OKEY! Archivo cargado correctamente")

# Mostrando las primeras filas del dataframe
#print(df.head())

# Filtrando por año 2022
#resultado = df[df['year'] == 2022]
#resultado = df[df['State'] == 'Bihar']

#resultado = df['Election_ID'].count()
#resultado = df['Election_ID'].sum()

# Mostrando resultado
#print(resultado)

df=pd.read_csv("Vote_Ai.csv")

filtro_avanzado = df["State"].str.startswith('Ba', na =False)
df_filtrado = df[filtro_avanzado]
suma_dinero = df_filtrado["Age"].sum()

print("---- Reporte automatizado ----")
print(f"Monto analizado: USD {suma_dinero:.2f}millones")

#condicional
if Default_limite_alto := (suma_dinero > 500):
    print("¡Alreta! El monto total supera el limite establecido.")
    print("Requiere revision inmediata")
elif suma_dinero < 100:
    print("Aviso: mercado moderado/alto")
    print("Monitorear comportamiento prox trim")
else:
    print("Mercado estable, sin alertas por el momento")

#-------------------------------------
#Grafico de barras usando toda la DF    
#-------------------------------------
print("\n[Generando GRAFICO de Barras]")
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10,6))
sns.barplot(
    data=df,
    x="Party",
    y="Campaign_Spending_Cr",
    estimator=sum,
    errorbar=None,
    palette="magma",

)
plt.title("Comparativa de Mercado por tipo de hardware", fontsize=14)
plt.xticks(rotation=20)

#Guardo grafico generado
plt.savefig("grafico_barra.png", dpi=300)
plt.close()

print ("\n¡Hecho! Los gráficos se guardaron correctamente en tu carpeta")