#Si el modulo esta en el mismo directorio
import funciones.saludar as m_saludar 
#Si el modulo esta en otro directorio
import sys 

print(m_saludar.Saludar("Juan"))
#Python le da prioridad a los modulos que son nativos en caso de tener un modulo con el mismo nombre
print(sys.builtin_module_names)
#Nos muestra los directorios donde python busca los modulos
print(sys.path)
#Añadimos un directorio a la lista de directorios donde python busca los modulos
sys.path.append('c:\\Users\\Maxim\\OneDrive\\Documents\\Projects\\Others\\python-course\\modulos\\funciones')

import saludar as mod_saludar
print(mod_saludar.Saludar("Juan"))