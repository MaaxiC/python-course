#Forma no optima de sumar valores
# def suma(lista):
#     numeros_sumados = 0
#     for numero in lista:
#         numeros_sumados += numero
#     return numeros_sumados
# resultado_suma = suma([1, 2, 3, 4, 5])

#Utilizando el parametro *args
#Se utiliza para pasar un numero variable de argumentos, se usa al final de los parametros
def suma(nombre, *args):
    return f'{nombre}, la suma de tus numeros es: {sum(args)}'

resultado_suma = suma('Juan', 1, 2, 3, 4, 5)
print(resultado_suma)

#Otra forma de hacer lo mismo
def suma_total(numeros):
    return sum([*numeros])

resultado_suma_total = suma_total([1, 2, 3, 4, 5])
print(resultado_suma_total)