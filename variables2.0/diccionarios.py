diccionario = dict(nombre = 'Carlos', edad = 22, cursos = ['Python', 'Django', 'JavaScript'])

#Para crear datos vacios hay que usar las funciones dict(), list(), set(), tuple()

#Las listas no pueden ser claves de un diccionario porque son mutables
diccionario = {[1, 2, 3]: 'lista'} #Esto no se puede hacer, tampoco puede ser conjunto a menos que se use el frozenset

diccionario = {(1, 2, 3): 'tupla'}

#Crear un diccionario con fromkeys
#El primer valor es un iterable
diccionario = dict.fromkeys(['a', 'b', 'c']) #Crea un diccionario con las claves de la lista y el valor None
diccionario = dict.fromkeys(['a', 'b', 'c'], 0) #Crea un diccionario con las claves de la lista y el valor 0
