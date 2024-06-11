diccionario = {
    'nombre': 'Carlos',
    'edad': 22,
    'cursos': ['Python', 'Django', 'JavaScript']
}

#dict_item es un objeto iterable que contiene tuplas con la clave y el valor
#Devuelve el valor de la clave(Sive para iterar tambien)
claves = diccionario.keys()

valor = diccionario.get('nombre') #Ideal para evitar errores, te devuelve None si no existe la clave
valor = diccionario['nombre'] #Si no existe la clave, lanza un error
valor = diccionario.get('nombre', 'No se encontro la clave') 

#Elimina todas las claves y valores
diccionario.clear()

#Elimina la clave y su valor
diccionario.pop('nombre')

#obtiene un elemento dict_item iterable
diccionario_iterable = diccionario.items()