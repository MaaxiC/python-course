#Queremos crear algo pero no queremos definir que va a hacer ahora
# def saludar():
#     pass

class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def __str__(self):
        print('Persona')
        return f'Nombre: {self.nombre}, Edad: {self.edad}, Nacionalidad: {self.nacionalidad}'
    
    def saludar(self):
        print(f'Hola, soy {self.nombre}')
    
#Clase Empleado hereda de Persona
class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, sueldo):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.sueldo = sueldo

    def __str__(self):
        print('Empleado')
        return f'{super().__str__()}, Trabajo: {self.trabajo}, Sueldo: {self.sueldo}'
    
    def saludar(self):
        print(f'Hola, trabajo de {self.trabajo}')
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, notas, universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.notas = notas
        self.universidad = universidad
    
roberto = Empleado('Roberto', 25, 'Mexicano', 'Programador', 1000)

roberto.saludar()

class Artista(Persona):
    def __init__(self, nombre, edad, nacionalidad, habilidad):
        super().__init__(nombre, edad, nacionalidad)
        self.habilidad = habilidad
    
    def mostrar_habilidad(self):
        print(f'Mi habilidad es: {self.habilidad}')
   
#Herencia multiple     
class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa
        
    def mostrar_habilidad(self):
        return(f'No tengo XD')
        
    def presentarse(self):
        return(f'{super().mostrar_habilidad()}') #Ideal para llamar a metodos de la clase padre
    def presentarse2(self):
        return(f'{self.mostrar_habilidad()}')
    
roberto = EmpleadoArtista('Roberto', 25, 'Mexicano', 'Cantar', 1000, "PM Studios")

roberto.presentarse()

herencia = issubclass(EmpleadoArtista, Persona) #Devuelve True si la clase es subclase de la clase dada

instancia = isinstance(roberto, EmpleadoArtista) #Devuelve True si el objeto es instancia de la clase dada

#El orden de ejecucion de los metodos es el siguiente:
#1. Metodo de la clase actual
#2. Metodo de la primera clase que hereda (La primera clase que se pone en la herencia multiple)
#En caso de que el padre de la segunda clase que hereda sea diferente al padre de la primera clase que hereda, le da prioridad al padre de la primera clase que hereda
#3. Metodo de la segunda clase que hereda (La segunda clase que se pone en la herencia multiple)
#4. Metodo de la clase padre

print(EmpleadoArtista.mro()) #Devuelve el orden de ejecucion de los metodos

artista = Artista('Juan', 25, 'Mexicano', 'Cantar')

#Forma de ejecutar un metodo de mas arriba en la jerarquia
EmpleadoArtista.mostrar_habilidad(artista)