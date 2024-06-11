class Celular:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.conectividad = "5G" #Atributo por defecto (Estatico)

    def __str__(self):
        return f"{self.marca} {self.modelo} cuesta {self.precio}"
    
    def llamar(self):
        print(f"Llamando desde {self.marca} {self.modelo}...")

#Instanciar un objeto de la clase Celular    
celular1 = Celular("Samsung", "Galaxy S10", 1000) #Atributos de instancia
print(celular1)