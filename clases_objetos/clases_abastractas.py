#Es una especie de plantilla que se puede usar para crear clases a partir de ella.
#No se pueden crear instancias de una clase abstracta.
#Se pueden definir métodos abstractos, que deben ser implementados en las clases hijas.
#Se pueden definir propiedades abstractas, que deben ser implementadas en las clases hijas.
from abc import ABC, abstractmethod

# ABC es una clase que se puede heredar para crear clases abstractas.
class Persona(ABC):
    @classmethod
    @abstractmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
    # def __subclasshook__(cls, subclass):
    #     return (hasattr(subclass, 'saludar') and callable(subclass.saludar) and
    #             hasattr(subclass, 'despedirse') and callable(subclass.despedirse))
    
    @classmethod
    @abstractmethod
    def hacer_actividad(self):
        pass
    
    def presentarse(self):
        print(f'Hola, mi nombre es {self.nombre} y tengo {self.edad} años.')
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
    
    def hacer_actividad(self):
        print(f'Estoy estudiando {self.actividad}.')
        
class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
    
    def hacer_actividad(self):
        print(f'Estoy trabajando en el rubro de {self.actividad}.')
        
estudiante = Estudiante('Juan', 20, 'M', 'Programacion')
trabajador = Trabajador('Pedro', 30, 'M', 'Ingenieria')
estudiante.presentarse()
estudiante.hacer_actividad()
trabajador.presentarse()
trabajador.hacer_actividad()