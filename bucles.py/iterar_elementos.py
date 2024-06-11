animales = ['gato', 'perro', 'serpiente', 'elefante', 'tigre']
numeros = {1, 2, 3, 4, 5}
dias = ('lunes', 'martes', 'miercoles', 'jueves', 'viernes')

for animal in animales:
    print(f'El animal es: {animal}')
    
#Iterar sobre dos o mas listas al mismo tiempo (deben tener la misma longitud)
for animal, numero in zip(animales, numeros):
    print(f'El animal es: {animal} y el numero es: {numero}')

#Iterar sobre un rango (Desde 5 hasta 10 sin incluir el 10)
#Si le pasamos un solo parametro, empieza desde 0    
for num in range(5,10):
    print(num)

#Forma no optima de recorrer una lista (No funciona en conjuntos)
# for i in range(len(numeros)):
#     print(f'El numeros es: {numeros[i]}')

#Forma optima de recorrer una lista con su indice
#num es una tupla con el indice y el valor
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'El numero es: {valor} y su indice es: {indice}')

#Desempaquetar la tupla en el for
for num, i in enumerate(numeros):
    print(f'El numero es: {i} y su indice es: {num}')
    
#Usando el for/else
for dia in dias:
    print(dia)
else:
    print('Fin del bucle') #Se ejecuta siempre al finalizar el bucle
    
#Todo lo anterior funciona exactamente igual para tuplas y conjuntos