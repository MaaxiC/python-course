#El archivo se cierra automaticamente al salir del bloque with
# with open('archivos\\archivo_texto.txt', 'r', encoding='UTF-8'):
with open(r'C:\Users\Maxim\OneDrive\Documents\Projects\Others\python-course\archivos\archivo_texto.txt', encoding='UTF-8') as archivo:
    print(archivo.read())
    # for linea in archivo:
    #     print(linea, end='')