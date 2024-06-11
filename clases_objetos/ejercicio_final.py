import openai

openai.api_key = '' # Ingresar la API Key de OpenAI
system_init = '''Hace de cuenta que sos un analizador de sentimientos.
                 Yo te paso sentimientos y vos analizas el sentimiento de los mensajes
                 y me das una respuesta con al menos 1 caracter y como maximo 4 caracteres
                 SOLO RESPUESTAS NUMERICAS. Donde -1 es negativo, 0 es neutral y 1 es positivo.
                 Podes responder con Ints o Floats.'''
mensajes = [{"role": "system", "content": system_init}]

#\x1b[0;37m Vuelve al color blanco
#\x1b[1;31m Color en consola Rojo para negativo, 32 para verde, 33 para amarillo y 34 para azul

class Sentimiento:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
        
    def __str__(self):
        return '\x1b[1;{}m{}\x1b[0;37m'.format(self.color, self.nombre)

class AnalizadorDeSentimientos:
    def __init__(self, rangos):
        self.rangos = rangos
        
    def analizar_sentimiento(self, polaridad):
        for rango, sentimiento in self.rangos:
            if rango[0] <= polaridad <= rango[1]:
                return sentimiento
        return Sentimiento("Muy Positivo", 32)
    
rangos = [
    ((-1,-0.7), Sentimiento("Muy Negativo", 31)),
    ((-0.6,-0.3), Sentimiento("Negativo", 31)),
    ((-0.3,-0.1), Sentimiento("Algo Negativo", 31)),
    ((-0.1,0.1), Sentimiento("Neutral", 33)),
    ((0.1,0.3), Sentimiento("Algo Positivo", 32)),
    ((0.3,0.7), Sentimiento("Positivo", 32)),
]
        
analizador = AnalizadorDeSentimientos(rangos)
# resultado = analizador.analizar_sentimiento(1)
# print(resultado)

while True:
    user_prompt = input("Ingrese un mensaje: ")
    mensajes.append({"role": "user", "content": user_prompt})
    completion = openai.chat.completions.create(
        model ="gpt-3.5-turbo",
        messages = mensajes,
        max_tokens = 8
    )
    
    respuesta = completion.choices[0].message.content
    mensajes.append({"role": "assistant", "content": respuesta})
    
    sentimiento = analizador.analizar_sentimiento(float(respuesta))
    print(sentimiento)