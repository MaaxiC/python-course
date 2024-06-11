frutas = ['manzana', 'pera', 'mango', 'fresa', 'kiwi', 'piña', 'uva', 'naranja', 'sandía', 'melón']
numeros = [1, 2, 3, 4, 5]

for fruta in frutas:
    if fruta == 'piña':
        continue #Salta a la siguiente iteración sin ejecutar el código que sigue
    print(f'Las fruta es: {fruta}')
    
#Evitar que el bucle siga ejecutándose
for fruta in frutas:
    print(f'Las fruta es: {fruta}')
    if fruta == 'pera':
        break #Termina el bucle
else:
    print('Fin del bucle') #No se ejecuta porque el bucle se termina con break
print('Fin de la ejecución')

#Recorrer una cadena de texto
cadena = 'Hola Mundo'
for letra in cadena:
    print(letra)
    
#For en una sola linea
# numeros_duplicados = list()
# for numero in numeros:
#     numeros_duplicados.append(numero * 2)
numeros_duplicados = [numero * 2 for numero in numeros]
print(numeros_duplicados)