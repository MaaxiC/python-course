#Interface Segregation Principle
#Los clientes no deben ser forzados a depender de interfaces que no usan

from abc import ABC, abstractmethod

class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass
    
class Comedor(ABC):
    @abstractmethod
    def comer(self):
        pass

class Durmiente(ABC):
    @abstractmethod
    def dormir(self):
        pass
    
class Humano(Trabajador, Comedor, Durmiente):
    def comer(self):
        return 'Comiendo'
    
    def trabajar(self):
        return 'Trabajando'
    
    def dormir(self):
        return 'Durmiendo'
    
class Robot(Trabajador):
    def trabajar(self):
        return 'Trabajando'
    
robot = Robot()
trabajador = Trabajador()

print(robot.trabajar()) #Trabajando
print(trabajador.trabajar()) #Trabajando