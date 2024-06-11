# SRP: Single Responsibility Principle
class TanqueDeCombustible:
    def __init__(self, capacidad, nivel):
        self.capacidad = capacidad
        self.nivel = nivel

    def llenar(self, cantidad):
        if self.nivel + cantidad > self.capacidad:
            raise ValueError("No se puede exceder la capacidad del tanque")
        self.nivel += cantidad

    def vaciar(self, cantidad):
        if self.nivel - cantidad < 0:
            raise ValueError("No se puede vaciar más de lo que hay en el tanque")
        self.nivel -= cantidad

    def obtener_nivel(self):
        return self.nivel
    
class Auto:
    def __init__(self, tanque):
        self.tanque = tanque

    def conducir(self, distancia):
        consumo = distancia / 10
        self.tanque.vaciar(consumo)

tanque = TanqueDeCombustible(50, 20)
auto = Auto(tanque)
auto.conducir(100)
print(tanque.obtener_nivel()) #10