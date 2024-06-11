cadena1 = "Hola"
cadena2 = "Mundo"

#Devuelve la lista de métodos y atributos de un objeto (Funcion)
print(dir(cadena1))

#Mayusculas (Metodo)
print(cadena1.upper())
#Minusculas
print(cadena1.lower())
#Capitalizar
print(cadena1.capitalize())
#Busca una cadena dentro de otra (Devuelve la posición, empieza de 0, -1 si no lo encuentra)
print(cadena1.find("o"))
#Busca una cadena dentro de otra (Si no lo encuentra, lanza una excepción)
print(cadena1.index("x"))
#Si es un número devuelve True, si no False
print(cadena1.isnumeric())
#Si es alfabético devuelve True, si no False
print(cadena1.isalpha())
#Cuenta el número de veces que aparece una cadena dentro de otra
print(cadena1.count("o"))
#Cuenta el número de caracteres de una cadena
print(len(cadena1))
#Verifica si una cadena empieza por una cadena
print(cadena1.startswith("H"))
#Verifica si una cadena termina por una cadena
print(cadena1.endswith("a"))
#Reemplaza una parte de una cadena por otra sino se especifica el número de veces, se reemplaza todas las ocurrencias
#Si no se encuentra la cadena a reemplazar, devuelve la cadena original
print(cadena1.replace("o", "x"))
#Separa una cadena en una lista de cadenas
print(cadena1.split(","))