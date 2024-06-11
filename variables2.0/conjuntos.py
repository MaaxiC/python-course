conjunto = set(['hola', 2, 3.5, True, (1, 2, 3), {"nombre": "Juan", "edad": 25}])
#no se puede utilizar elementos mutables como listas o diccionarios, habria que convertirlos a tuplas

conjunto1 = {"dato1", "dato2"}
#No se puede poner un conjunto dentro de otro conjunto
conjunto2 = {conjunto1, "dato3"}
#Hay que usar esta funcion para unir conjuntos
conjunto2 = frozenset(["dato1", "dato2"]) #Crea un conjunto inmutable

#Teoria de conjuntos
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}

resultado = conjunto2.issubset(conjunto1) #Devuelve True si el conjunto2 es subconjunto de conjunto1
resultado = conjunto2 <= conjunto1 #Otra forma de hacer lo mismo

resultado = conjunto1.issuperset(conjunto2) #Devuelve True si el conjunto1 es superconjunto de conjunto2
resultado = conjunto2 > conjunto1 #Otra forma de hacer lo mismo

#Verificar si hay algun elemento en comun
resultado = conjunto2.isdisjoint(conjunto1) #Devuelve True si no hay elementos en comun