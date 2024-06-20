import random
import string

def generar_claves(numero_caracteres,numero_claves):
    contador_claves = 0
    while contador_claves < numero_claves:
        cadena = ""
        contador_caracter = 0
        while contador_caracter < numero_caracteres:
            caracter = random.choice(string.ascii_lowercase + string.digits)
            cadena += caracter
            contador_caracter += 1
        print(cadena)
        contador_claves += 1

def rgb_color_gen():
    contador = 0
    componentes = []
    while contador < 3:
        componente = str(random.randint(0,255))
        componentes.append(componente)
        contador += 1
    cadena = ",".join(componentes) 
    cadena_final = "(" + cadena + ")"
     
    print(cadena_final)
   


        
       
    
        
    