import re

text = '''Hola, mi nombre es Juan y mi número de teléfono es 1234567890
Esta es una prueba de expresiones regulares
Linea final r'(\d{10})'
'''

#Haciendo busquedas simmples
resultado = re.search("mi", text) #Devuelve un objeto con la primera coincidencia
resultado = re.findall("mi", text) #Devuelve una lista con todas las coincidencias
resultado = re.findall("mi", text,flags=re.IGNORECASE) #Devuelve una lista con todas las coincidencias, sin importar mayúsculas o minúsculas

#\d -> Busca cualquier dígito
resultado = re.findall(r"\d", text) #Indico que es un raw string para que no interprete el backslash

#\D -> Busca todo menos dígitos
resultado = re.findall(r"\D", text)

#w -> Busca cualquier caracter alfanumérico [a-zA-Z0-9_], para Python _ es un caracter alfanumérico
resultado = re.findall(r"\w", text)

#W -> Busca todo menos caracteres alfanumérico [a-zA-Z0-9_]
resultado = re.findall(r"\W", text)

#s -> Busca espacios en blanco [\t\n\r\f\v] [espacio, tabulador, nueva linea, retorno de carro, salto de página, tabulación vertical]
resultado = re.findall(r"\s", text)

#S -> Busca todo menos espacios en blanco [\t\n\r\f\v] [espacio, tabulador, nueva linea, retorno de carro, salto de página, tabulación vertical]
resultado = re.findall(r"\S", text)

#. -> Busca cualquier caracter excepto nueva linea
resultado = re.findall(r".", text)

#/n -> Busca nueva linea
resultado = re.findall(r"\n", text)

#^ -> Busca el inicio de una cadena (Verifica si la cadena comienza con el texto que se busca)
resultado = re.findall(r"^Hola", text)
resultado = re.findall(r"^Hola", text, flags=re.MULTILINE) #Busca el inicio de una cadena en cada linea

#$ -> Busca el final de una cadena
resultado = re.findall(r"Linea final$", text)

#[] -> Busca cualquier caracter dentro de los corchetes (No importa que no estén juntos)
resultado = re.findall(r"[aeiou]", text)

#\ -> Caracter de escape (Cancelar funcionalidad de caracter especial, lo interpreta como un caracter normal)
resultado = re.findall(r"\.", text)

#Armando una cadena que busque un numero, seguido de un punto y un espacio
resultado = re.findall(r"\d\.\s", text)


#Grupos

#{n} -> Busca n cantidad de veces del caracter anterior (Deben estar seguidos)
resultado = re.findall(r"\d{10}", text)

#{n, m} -> Busca entre n y m cantidad de veces del caracter anterior (Si hay mas numeros lo va partiendo en grupos de n)
resultado = re.findall(r"\d{1,10}", text)

#Conjuntos de caracteres
resultado = re.findall(r"ab{1,10}", text) #Busca a seguido de b entre 1 y 10 veces, solo afecta a la b
resultado = re.findall(r"(ab){1,10}", text) #Busca a seguido de b entre 1 y 10 veces, afecta al grupo (ab)
resultado = re.findall(r"(ab){2}", text) #Si encuentra abab 2 veces, devuelve 1 ab
resultado = re.findall(r"[ab]{2}", text) #Los corchetes buscan a o b 2 veces (aa, ab, ba, bb)

#Operadores
#| -> Busca una cadena o la otra (Devuelve las coincidencias de ambas, en el orden en que las encuentra)
resultado = re.findall(r"mi|Juan", text)

#* -> Busca 0 o más coincidencias del caracter anterior (Si no encuentra el caracter, devuelve vacio sino devuelve todas las coincidencias)
resultado = re.findall(r"mi*", text)

#+ -> Busca 1 o más coincidencias del caracter anterior (Al menos una vez debe estar el caracter, devuelve todas las coincidencias)
resultado = re.findall(r"mi+", text)

#? -> Busca 0 o 1 coincidencia del caracter anterior (Puede estar o no estar el caracter)
resultado = re.findall(r"mi?", text)

#- -> Sive para hacer separaciones en rangos (Solo afecta a los caracteres que estén dentro de los corchetes)
resultado = re.findall(r"[a-z]", text) #Busca cualquier letra minúscula

#% -> Todo lo que encuentre antes de % y después de % lo devuelve

print(resultado)

#Reemplazar todas las coincidencias del patrón en la cadena
resultado = re.sub(r"mi", "tu", text)

#Verificar si coincide
resultado = re.match(r"Hola", text)