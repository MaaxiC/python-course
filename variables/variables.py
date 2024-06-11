a = 2
b = 3
c = a + b
c += 1
print(c)


nombre = "Juan"
bienv = "Hola, " + nombre
print(bienv)

#Concatenación de strings con f-strings
nombre = "Juan"
bienv = f"Hola {nombre} ¿Cómo estás?"
print(bienv)

del bienv

#Operadores de pertenencia
print("J" in bienv) #True
print("J" not in bienv) #False

#Es case sensitive

#Camel Case
nombreCompleto = "Juan Pérez"

#Snake Case
nombre_completo = "Juan Pérez"

print(type(nombre_completo))