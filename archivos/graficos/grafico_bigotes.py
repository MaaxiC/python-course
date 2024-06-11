import pandas as pd
import matplotlib.pyplot as plt #Librería de visualización de datos (Gráficos)
import seaborn as sns #Librería de graficos estadisticos
#Obtener el directorio actual
# import os
# print(os.getcwd())

df = pd.read_csv("archivos\\graficos\\bigotes.csv")

#Crear un gráfico de dispersión
sns.boxplot(data=df, x="categoria", y="valor")

plt.show()  