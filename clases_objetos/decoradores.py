# Definición de un decorador
# Un decorador es una función que recibe como parámetro otra función, le agrega una funcionalidad antes o despues de ejecutarla y despues retorna una nueva función.
def decorador(funcion):
    def nueva_funcion():
        print("Se ejecutará la función")
        funcion()
        print("Se ha ejecutado la función")
    return nueva_funcion

# def saludo():
#     print("Hola")

# saludo = decorador(saludo)
# saludo()

@decorador
def saludo():
    print("Hola")
    
saludo()