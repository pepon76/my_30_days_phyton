# Ejercicio 1: Par o Impar
# Escribe una función llamada es_par que tome un número como entrada y devuelva True si es par y False si es impar.

# def es_par(numero):
#     if numero%2 == 0:
#         print(f"el numero {numero} es par")
#     else:
#         print(f"el numero {numero} es impar")
    
# es_par(15)

# # Ejercicio 2: Calificación de un Estudiante
# # Escribe una función llamada calificar_estudiante que tome una puntuación como entrada y devuelva la calificación correspondiente de acuerdo con la siguiente tabla:

# # Puntuación >= 90: "A"
# # 80 <= Puntuación < 90: "B"
# # 70 <= Puntuación < 80: "C"
# # 60 <= Puntuación < 70: "D"
# # Puntuación < 60: "F"

# def calificar_estudiante(puntuacion):
#     if puntuacion >= 90:
#         print(f"La calificacion es: \"A\"")
#     elif 80 <= puntuacion < 90: 
#         print(f"La calificacion es: \"B\"")
#     elif 70 <= puntuacion < 80: 
#         print(f"La calificacion es: \"C\"")
#     elif 60 <= puntuacion < 70: 
#         print(f"La calificacion es: \"D\"")
#     else:
#         print(f"La calificacion es: \"F\"")
        
# calificar_estudiante(60)

# # Ejercicio 4: Mayor de Tres Números
# # Escribe una función llamada mayor_de_tres que tome tres números como entrada y devuelva el mayor de los tres.
# def mayor_3(num1,num2,num3):
#     if num1 > num2:
#         if num2 > num3:
#             print(f"El numero mayor es {num1}")


# def tipo_triangulo(lado1,lado2,lado3):
#     if lado1 == lado2 == lado3:
#         print("equilatero")
#     elif lado1 != lado2 and lado1!= lado3 and lado2!=lado3:
#         print("escaleno")
#     else:
#         print("isosceles")
        
# tipo_triangulo(4,3,1)

frutas = []

while True:
    fruta = input(str("Escribe una fruta para añadirla a el carrito:"))
    if fruta in frutas:
        print("La fruta ya esta en la lista")
    else:        
        frutas.append(fruta)
        print("Fruta añadida al carrito:", fruta)
        print("Frutas en el carrito:", frutas)
    
    
   
        
        
    
        
        