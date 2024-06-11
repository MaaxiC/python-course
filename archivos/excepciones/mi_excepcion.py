# Creacion de excepciones personalizadas
class MiExcepcion(Exception):
    def __init__(self, err):
        print("Impresionante, cometiste el siguiente error: ", err)
        # super().__init__(self.mensaje)

#Lanzamiento de excepciones personalizadas
#raise MiExcepcion("Error personalizado") 

#Manejo de excepciones personalizadas      
try:
    raise MiExcepcion("Error personalizado")
except:
    print("Como vas a cometer ese error?")