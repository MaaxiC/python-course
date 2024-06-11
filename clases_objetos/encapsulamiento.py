# Encapsulamiento: Es la propiedad de los objetos que permite ocultar los atributos y métodos internos de un objeto y mostrar solo lo que es necesario para el usuario.
class MiClase:
    def __init__(self, valor):
        self.__atributo = valor #Encapsulamiento, con el doble guion bajo se hace privado el atributo

    def get_atributo(self):
        return self.__atributo

    def set_atributo(self, valor):
        self.__atributo = valor
        
    def __metodo_privado(self):
        print('Soy un método privado')
        
objeto = MiClase("Hola")
print(objeto.get_atributo())
objeto.set_atributo("Nuevo valor")
print(objeto.get_atributo())