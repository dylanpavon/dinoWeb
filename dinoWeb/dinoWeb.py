import openai
import key

openai.api_key =  key.api

system_rol = '''Hace de cuenta que sos un dinosaurio cuya especie te voy a pasar por parámetro con la función conversar(nombre).
                 Apenas te hable, debes presentarte como tal y es importante que no hables de otras especies de dinosaurio 
                 que no sea la tuya. 
                 Te voy a hacer una pregunta respecto a vos (por ejemplo que comes, donde vives) 
                 y me tenés que responder como si fueras la especie del dinosaurio en cuestión.
                 Solo responde preguntas relacionadas al dinosaurio que representas.'''
        
mensajes =[{"role": "system", "content": system_rol}]

class Dino:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        
class DinoServicios:
    def __init__(self, dino: Dino):
        self.dino = dino
    
    def conversar(self, nombre):
        self.dino.nombre = nombre
        
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
            
t_rex = Dino("Tiranosaurio Rex", ".")
chat = DinoServicios(t_rex)
chat.conversar(t_rex.nombre)
   
