#Liskov Substitution Principle
#La subclase debe poder ser sustituida por la clase base
# class Ave:
#     def volar(self):
#         return 'Volando'

# class Pinguino(Ave):
#     def volar(self):
#         return 'No puedo volar'
    
# def hacer_volar(ave = Ave):
#     return ave.volar()

class Ave:
    pass

class AveVoladora(Ave):
    def volar(self):
        return 'Volando'

class AveNoVoladora(Ave):
    pass

class Pinguino(AveNoVoladora):
    def volar(self):
        return 'No puedo volar'
    
def hacer_volar(ave = Pinguino):
    return ave.volar()

pinguino = Pinguino()
print(hacer_volar(pinguino)) #No puedo volar