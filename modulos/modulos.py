#Namespace
import modulo_saludar as m_saludar #Importamos el modulo completo
from modulo_saludar import Saludar, Saludar2 as Otra_funcion #Importamos las funciones específicas

saludo = m_saludar.Saludar("Juan")
saludo1 = Saludar("Juan")
saludo2 = Otra_funcion("Juan")
print(saludo2)

#Para ver los métodos y atributos de un módulo
print(dir(m_saludar))

#Accedemos al nombre del modulo
print(__name__)

#Accedemos al nombre del módulo llamado
print(m_saludar.__name__)