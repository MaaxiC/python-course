
#Lista
lista = ["hola", 2, 3.5, True, [1, 2, 3], {"nombre": "Juan", "edad": 25}]

#Tupla
tupla = ("hola", 2, 3.5, True, [1, 2, 3], {"nombre": "Juan", "edad": 25}) #No se pueden modificar

print(lista)
print(lista[0])
print(tupla[1])

#Set (Conjunto, son datos desordenados)
#No se puede modificar un elemento pero si redefinir el conjunto
#No se puede acceder por el indice a un elemento del conjunto
#No puede haber elementos duplicados, se ignoran los repetidos
#Se puede iterar
conjunto = {"hola", 2, 3.5, True, [1, 2, 3], {"nombre": "Juan", "edad": 25}}
conjunto = {"chau", 2, 3.5, True, [1, 2, 3], {"nombre": "Juan", "edad": 25}}

#Diccionario
diccionario = {
    "nombre": "Juan", 
    "edad": 25
}
print(diccionario["nombre"])