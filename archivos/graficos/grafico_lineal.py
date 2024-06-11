import pandas as pd
import matplotlib.pyplot as plt #Librería de visualización de datos (Gráficos)
import seaborn as sns #Librería de graficos estadisticos
#Obtener el directorio actual
# import os
# print(os.getcwd())

df = pd.read_csv("archivos\\graficos\\datos.csv")

sns.lineplot(data=df, x="fecha", y="cantidad")

#Creando un punto en el gráfico
# plt.plot(df["fecha"], df["cantidad"], marker='o', color='r')
plt.plot('01-09', 17, marker='o', color='r')

plt.show()  