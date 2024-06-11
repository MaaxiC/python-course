diccionario = {
    'nombre': 'Carlos',
    'edad': 22,
    'cursos': ['Python', 'Django', 'JavaScript']
}

#Recorrer el diccionario para obtener las claves
for clave in diccionario:
    print(clave)

#Recorrer el diccionario con items para obtener las tupla (clave, valor)    
for tupla in diccionario.items():
    print(tupla)

for clave, valor in diccionario.items():
    print(clave, valor)