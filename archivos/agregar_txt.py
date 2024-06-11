#Si no existe el archivo, lo crea
#Absolute Path
with open(r'C:\Users\Maxim\OneDrive\Documents\Projects\Others\python-course\archivos\archivo_texto.txt', "a", encoding='UTF-8') as archivo:
    #Agrego al archivo sin sobreescribir al ser Append
    archivo.write("Hola mundo\n")   