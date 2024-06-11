# OCP: Open/Closed Principle
#Abierto para extensión, cerrado para modificación
class Notificador:
    def __init__(self, usuaio, mensaje):
        self.usuario = usuaio
        self.mensaje = mensaje
    def notificar(self):
        raise NotImplementedError
    
class NotificacionPorEmail(Notificador):
    def notificar(self):
        return f'Notificando a {self.usuario} por email: {self.mensaje}'
    
class NotificacionPorSMS(Notificador):
    def notificar(self):
        return f'Notificando a {self.usuario} por SMS: {self.mensaje}'