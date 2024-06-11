#Son Getter, Setter y Deleter
#Son métodos que permiten obtener, modificar y eliminar el valor de un atributo de una clase.
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre
        
    @nombre.deleter
    def nombre(self):
        del self.__nombre
        
objeto = Persona("Maximiliano", 25)

nombre = objeto.nombre
print(nombre)

objeto.nombre = "Max"
nombre = objeto.nombre
print(nombre)

del objeto.nombre