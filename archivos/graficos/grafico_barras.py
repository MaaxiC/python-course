import pandas as pd
import matplotlib.pyplot as plt #Librería de visualización de datos (Gráficos)
import seaborn as sns #Librería de graficos estadisticos
#Obtener el directorio actual
# import os
# print(os.getcwd())

df = pd.read_csv("archivos\\graficos\\ingresos.csv")

#Crear un gráfico de barras
sns.barplot(data=df, x="fuente", y="ingresos")

total_ingresos = df["ingresos"].sum()

print(f'Total de ingresos: ${total_ingresos} USD')

plt.show()  