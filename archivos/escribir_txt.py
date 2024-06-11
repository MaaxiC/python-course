nombre = ["Maximiliano", "Juan", "Pedro", "Maria"]
apellido = ["Gomez", "Perez", "Gonzalez", "Lopez"]

#Si no existe el archivo, lo crea
#Absolute Path
with open(r'C:\Users\Maxim\OneDrive\Documents\Projects\Others\python-course\archivos\archivo_texto.txt', "w", encoding='UTF-8') as archivo:
    #Sobreescribe el archivo
    archivo.write("Hola mundo\n")
    #Añade al final del archivo (Le pasas una lista con las lineas)
    archivo.writelines(["Segunda linea\n", "Tercera linea\n"])
    archivo.writelines(["Cuarta linea\n", "Quinta linea\n"])
    [archivo.writelines(f"Nombre: {n}\nApellido: {a}\n\n") for n,a in zip(nombre, apellido)]
#Es lo mismo que:
# for n,a in zip(nombre, apellido):
#     archivo.writelines(f"Nombre: {n}\nApellido: {a}\n\n")