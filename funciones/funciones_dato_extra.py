#Funcion con parametro Opcional (Si no se pasa el argumento, se toma el valor por defecto)
def frase(nombre, apellido, adjetivo = "triste"):
    print(f"{nombre} {apellido} es {adjetivo}")
    
#Forzar un argumento, se puede cambiar el orden
#keyword argument
frase_resultante = frase(adjetivo ="feliz", nombre="Juan", apellido="Perez")
print(frase_resultante)