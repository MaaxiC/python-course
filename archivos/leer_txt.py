open('archivos\\archivo_texto.txt', 'r') #Abrir archivo en modo lectura
archivo = open(r'C:\Users\Maxim\OneDrive\Documents\Projects\Others\python-course\archivos\archivo_texto.txt', encoding='UTF-8') #Abrir archivo

#Leer archivo completo
# archivo = archivo.read() 
#Una vez que se lee el archivo, no se puede volver a leer porque no lo cerramos
#Leer linea por linea
# lineas = archivo.readlines()
#Leer una sola linea
#Si le paso un número, lee esa cantidad de caracteres
linea = archivo.readline()
#Cuando son archivos grandes hay que usar otra solucion para evitar que se llene la memoria 

#Cerrar archivo
archivo.close()

print(linea)