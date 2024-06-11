numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Encontrando el numero mayor de una lista (Tiene que ser numeros)
numero_mayor = max(numeros)
print(numero_mayor)

#Encontrando el numero menor de una lista (Tiene que ser numeros)
numero_menor = min(numeros)
print(numero_menor)

#Redondeando a 2 decimales (Por defecto redondea a 0 decimales)
numero = round(3.14159265359, 2)
print(numero)

#Retorna False -> 0, None, '', [], {}, set() / True -> cualquier otro valor
resultado_bool = bool(0)
print(resultado_bool)

#Retorna True si todos los elementos de la lista son True
resultado_all = all(numeros)
print(resultado_all)

#Suma todos los elementos de la lista (Tiene que ser numeros)
suma = sum(numeros)