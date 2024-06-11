import pandas as pd
#names es un parámetro que se le pasa a read_csv para que tome la primera fila como los nombres de las columnas
#DataFrame, estructura de datos bidimensional, similar a una hoja de cálculo
# df = pd.read_csv(r'C:\Users\Maxim\OneDrive\Documents\Projects\Others\python-course\archivos\archivo_csv.csv', names=["name", "lastname", "age"])
df = pd.read_csv(r'C:\Users\Maxim\OneDrive\Documents\Projects\Others\python-course\archivos\archivo_csv.csv') #DataFrame, estructura de datos bidimensional, similar a una hoja de cálculo
df2 = pd.read_csv(r'C:\Users\Maxim\OneDrive\Documents\Projects\Others\python-course\archivos\archivo_csv.csv') #DataFrame, estructura de datos bidimensional, similar a una hoja de cálculo
nombres = df["Nombre"] #Imprime la columna "Nombre"

cadena = "0123456789"
print(cadena[0:5]) #Imprime los primeros 5 caracteres de la cadena (Slice) (Sin incluir el último)

#ordenamos el DataFrame por la columna "Edad"
df_ordenado_asc = df.sort_values("Edad")

#Ordenando de forma descendente
df_ordenado_desc = df.sort_values("Edad", ascending=False)

#Concatenando dos DataFrames
df_concatenado = pd.concat([df, df2])

#Accediendo a la primera fila del DataFrame
primer_fila = df.head(1)
#Accediendo a las primeras 2 filas del DataFrame
primer_y_segunda_fila = df.head(2)

#Accediendo a las últimas filas del DataFrame
ultimas_filas = df.tail(2)

#Accediendo a la cantidad de filas y columnas del DataFrame
#La función shape devuelve una tupla con la cantidad de filas y columnas
cantidad_filas_columnas = df.shape
filas_totales, columnas_totales = cantidad_filas_columnas

#Obteniendo data estadística del DataFrame
data_estadistica = df.describe()

#Accediendo a un elemento específico del DataFrame
# elemento_especifico = df.loc[0, 0] #Accede al elemento en la fila 0, columna 0
elemento_especifico = df.loc[1, "Apellido"]

#Accediendo a un elemento específico del DataFrame solo con los indices
elemento_especifico = df.iloc[1, 1]

#Accediendo a todas las filas de una columna específica
apellidos = df.iloc[:,1] #Con Slice

#Accediendo a todas las columnas de una fila específica
apellidos = df.loc[1,:] #Con Slice
apellidos = df.iloc[1,:] #Funciona igual que con loc

#Accediendo a filas con edad mayor a 25
mayores_30 = df[df["Edad"] > 25]
#mayores_30 = df.loc[df["Edad"] > 25,:] #Funciona igual 

#Cambiar el tipo de dato de una columna
df["Edad"] = df["Edad"].astype(str)
print(type(df["Edad"][0]))

#Reemplazar valores en una columna
df["Nombre"] = df["Nombre"].replace("Carlos", "Juan", inplace=True)

#Eliminar las filas con datos faltantes(Vacios)
df = df.dropna()

#Eliminar las filas repetidas
df = df.drop_duplicates()

#Crear un csv con el DataFrame resultante (limpio)
df.to_csv(r'C:\Users\Maxim\OneDrive\Documents\Projects\Others\python-course\archivos\archivo_csv_limpio.csv', index=False)
