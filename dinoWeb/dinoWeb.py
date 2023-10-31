import openai
import key

openai.api_key =  key.api

# system_rol = '''Hace de cuenta que sos un dinosaurio cuya especie te voy a pasar por parámetro con la función conversar(nombre).
#                  Apenas te hable, debes presentarte como tal y es importante que no hables de otras especies de dinosaurio 
#                  que no sea la tuya. 
#                  Te voy a hacer una pregunta respecto a vos (por ejemplo que comes, donde vives) 
#                  y me tenés que responder como si fueras la especie del dinosaurio en cuestión.
#                  Solo responde preguntas relacionadas al dinosaurio que representas.'''
        
# mensajes =[{"role": "system", "content": system_rol}]

class Dino:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        
class DinoServicios:
    def __init__(self, dino: Dino):
        self.dino = dino
    
    def conversar(self, nombre, descripcion):
        self.dino.nombre = nombre
        #self.system_rol = system_rol
        self.dino.descripcion = descripcion
        while True:
            system_rol = f'''Hace de cuenta que sos un dinosaurio {nombre}
                 Te voy a hacer una pregunta respecto a ti (por ejemplo que comes, donde vives) 
                 y me tenés que responder como si fueras el {nombre}.
                 Puedes usar esta información como referencia: {descripcion}'''
        
            mensajes =[{"role": "system", "content": system_rol}]
            user_prompt = input("Preguntame>> ")
            mensajes.append({"role": "user", "content": user_prompt})
    
            if user_prompt == "0":
                print("Muchas gracias! Un gusto conversar contigo!")
                break

            completion = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = mensajes,
            max_tokens = 200
            )
        
            respuesta = completion.choices[0].message["content"]
            print(respuesta)
            mensajes.append({"role": "assistant", "content": respuesta})
            
t_rex = Dino("Triceratops", "El famoso dinosaurio herbívoro de tres cuernos.")
chat = DinoServicios(t_rex)
chat.conversar(t_rex.nombre, t_rex.descripcion)
   
