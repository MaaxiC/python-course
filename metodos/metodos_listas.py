#Crea una lista con list, principalmente para una lista vacía
lista = list([1, 2, 3, 4, 5])

#Devuelve la cantidad de elementos de una lista
print(len(lista))

#Modifica la lista original
#Agregar un elemento a la lista
print(lista.append(6)) 
#Agregar un elemento a la lista en una posición específica
print(lista.insert(0, 5))
#Agregar varios elementos a la lista
print(lista.extend([7, 8, 9]))
#Eliminar un elemento de la lista por su indice
print(lista.pop(0)) #Con -1 elimina el último elemento, con -2 el anteultimo, etc.
#Eliminar un elemento de la lista por su valor
print(lista.remove(5)) #Si no encuentra el valor, lanza una excepción
#Eliminar todos los elementos de la lista
print(lista.clear())
#Ordenar la lista (Si son números, los ordena de menor a mayor, si son letras, las ordena alfabéticamente)
#Si se le pasa el parámetro reverse=True, los ordena de mayor a menor
#No puede ordenar listas con elementos de diferentes tipos (números y letras)
print(lista.sort())
print(lista.sort(reverse=True))
#Invertir la lista
print(lista.reverse())

#Devuelve el indice del elemento en la lista
print(lista.index(5)) #Si no lo encuentra, lanza una excepción

#Con las tuplas se puede buscar elementos o contarlos, pero no se pueden modificar