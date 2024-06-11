#Dependency Inversion Principle
#Las clases de alto nivel no deben depender de las clases de bajo nivel

from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self, palabra):
        pass
    
class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        #Logica para verificar la ortografía de una palabra en un diccionario
        pass
    
class ServcioWeb(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        #Logica para verificar la ortografía de una palabra en un servicio web
        pass
    
class CorrectorOrtografico:
    def __init__(self, verificador):
        self.verificador = verificador
        
    def corregir_texto(self, palabra):
        #Logica para corregir la ortografía de un texto
        return self.verificador.verificar_palabra(palabra)
    
corrector = CorrectorOrtografico(Diccionario())
corrector = CorrectorOrtografico(ServcioWeb())