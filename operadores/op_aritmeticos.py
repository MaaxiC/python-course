suma = 12 + 5
resta = 12 - 5
multiplicacion = 12 * 5
division = 12 / 5 #Siempre devuelve un float
division_entera = 12 // 5 #Devuelve un entero redondeado hacia abajo
modulo = 12 % 5 #Resto de la division
potencia = 12 ** 5

tipo_de_dato = type(suma)

duracion = 1.5
otro_curso = 7

#Cuando se quiere reducir la cantidad de decimales se puede usar //
#Termina quedando con un decimal, porque pasas la coma y despues la volves a poner
# diferencia_con_max = 100 - duracion * 1000 // otro_curso / 10
diferencia_con_max = round(100 - duracion * 100 / otro_curso, 1)
#Para 2 decimales
# diferencia_con_max = 100 - duracion * 10000 // otro_curso / 100
print(f'La diferencia con max es: {diferencia_con_max}')