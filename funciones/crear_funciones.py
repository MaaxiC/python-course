# Crear funciones en Python
def saludar():
    print("Hola, bienvenido a mi programa")
    
saludar()

def saludar(nombre, sexo):
    sexo = sexo.lower()
    if sexo == "mujer":
        adjetivo = "reina"
    elif sexo == "hombre":
        adjetivo = "titan"
    else:
        adjetivo = "crack"
    print(f"Hola {nombre}, mi {adjetivo}, bienvenido a mi programa")

saludar("Juan", "hombre")

#Crear una funcion que nos retorne valores
def crear_contrasena_random(num):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    num_string = str(num)
    num = int(num_string[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contrasena = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contrasena, num #Devuelve una tupla

#Desempaquetar tupla
password, primer_numero = crear_contrasena_random(5)
print(f'La contraseña es: {password}')
print(f'El primer número es: {primer_numero}')