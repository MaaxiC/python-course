class Persona:
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
    
    #Devuelve como se debe imprimir la instancia.
    def __str__(self):
        return f'Nombre: {self.nombre}, Edad: {self.edad}, Sexo: {self.sexo}, Actividad: {self.actividad}'
    
    #Devuelve una representación de la instancia en forma de cadena.
    def __repr__(self):
        return f'Persona("{self.nombre}", {self.edad}, "{self.sexo}", "{self.actividad}")'
    
    #Suma las edades de dos instancias de la clase. (Sobrecarga de operadores)
    def __add__(self, other):
        return Persona('Suma', self.edad + other.edad, 'M', 'Suma')
        
objeto = Persona('Juan', 20, 'M', 'Programacion')
objeto2 = Persona('Martin', 30, 'M', 'Cine')
print(objeto) #Nombre: Juan, Edad: 20, Sexo: M, Actividad: Programacion

repre = repr(objeto)
resultado = eval(repre) #Eval evalua si es una expresion valida en python
print(resultado) #Persona(Juan, 20, M, Programacion)
nueva_persona = objeto + objeto2
print(nueva_persona) #50

#Podemos definir como se van a comportar los operadores en nuestras clases con los métodos especiales. (Sobrecarga de operadores)