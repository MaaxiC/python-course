numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Lambda - Funcion anonima (No tiene nombre)
multiplicar_por_dos = lambda x : x * 2

#Usando filter
#Devuelve los elementos que cumplan con la condicion
#Hay que pasarle una funcion y un iterable
numeros_pares = filter(lambda numero : numero % 2 == 0, numeros)
print(list(numeros_pares))

#Ejericio
def obtener_alumnos(cantidad):
    alumnos = []
    for i in range(cantidad):
        nombre = input('Ingrese el nombre del alumno: ')
        edad = int(input('Ingrese la edad del alumno: '))
        alumno = nombre, edad
        alumnos.append(alumno)
    alumnos.sort(key=lambda x : x[1]) #Ordena por la edad
    #El asistente es el primer alumno y el profesor es el último, recupero el nombre
    asistente = alumnos[0][0]
    profesor = alumnos[-1][0]
    return asistente, profesor
    
asistente, profesor = obtener_alumnos(3)

print(f'El profesor es: {profesor} y su asistente es: {asistente}')

# def fibonacci(n):
#     fib = [0, 1]
#     [fib.append(fib[i - 1] + fib[i - 2]) for i in range(2, n)]
#     return fib

def fibonacci_2(num):
    a,b = 0,1
    fibonacci_lista = [0]
    for i in range(num):
        if b > num: return fibonacci_lista
        else:
            fibonacci_lista.append(b)
            a,b = b,a+b
            
resultado = fibonacci_2(100)
print(resultado)