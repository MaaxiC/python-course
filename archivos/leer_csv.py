import csv

with open(r'C:\Users\Maxim\OneDrive\Documents\Projects\Others\python-course\archivos\archivo_csv.csv', "r", encoding='UTF-8') as archivo:
    reader = csv.reader(archivo)
    for linea in reader:
        print(linea)