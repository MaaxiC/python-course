class Gato():
    def sonido(self):
        return 'dice: Miau!'

class Perro():
    def sonido(self):
        return 'dice: Guau!'
    
def sonido_animal(animal):
    print(animal.sonido())

gato = Gato()
perro = Perro()

print(gato.sonido())
print(perro.sonido())

sonido_animal(gato)

#En Python no se necesita que las clases tengan una relación de herencia para poder usar polimorfismo ya que es de tipado dinamico
#En el caso de lenguajes estaticos se necesita una interfaz o una herencia

#Polimorfismo de inclusión (Duck Typing)
#No importa si el objeto es de una clase en especifico, si tiene el metodo que se necesita, se puede usar

#Polimorfismo de herencia
#Se necesita que las clases tengan una relación de herencia para poder usar polimorfismo

#Polimorfismo de sobrecarga o overloading
#En python no existe como tal, pero se puede simular con argumentos por defecto 

#Polimorfismo de coerción o casting
numero = 5 #int
numero2 = 3.5 #float
resultado = numero + numero2