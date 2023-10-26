# comentario de Eze

import openai

openai.api_key = "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" 

system_rol = '''Hace de cuenta que sos un dinosaurio. Con alguna variable, te voy a indicar qué dinosaurio representas.
                Te voy a hacer una pregunta respecto a vos (por ejemplo que comes, donde vives) 
                y me tenés que responder como si fueras el dinosaurio en cuestión.
                Como máximo, utilizá 200 caracteres para responder. Solo responde preguntas relacionadas al dinosaurio que representas'''
        
mensajes =[{"role": "system", "content": system_rol}]

class Dino:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        
t_rex = Dino("Tiranosaurio Rex", ".")
        
while True:
    user_prompt = input("Preguntame>> ")
    mensajes.append({"role": "user", "content": user_prompt})
    
    if user_prompt == ".":
        break

    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = mensajes,
        max_tokens = 200
    )
        
    respuesta = completion.choices[0].message["content"]
    print(respuesta)
    mensajes.append({"role": "assistant", "content": respuesta})
    