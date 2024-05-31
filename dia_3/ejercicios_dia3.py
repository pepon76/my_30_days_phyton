# Declare your age as integer variable
age = int(45)
# Declare your height as a float variable
height = float(1.72)
# Declare a variable that store a complex number
num_complejo = complex(2 +2j)
# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h)
# base = float(input("Introduzca la base del triangulo: "))
# altura = float(input("Introduzca la altura del triangulo: "))
# area_triangulo = round(base * altura * 0.5,2)
# print(f"El area del triangulo es {area_triangulo}")

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c)

# side_a = float(input("Introduzca lado a: "))
# side_b = float(input("Introduzca lado b: "))
# side_c = float(input("Introduzca lado c: "))
# perimetro_triangulo = side_a + side_b + side_c
# print(f"El perimetro del triangulo es {perimetro_triangulo}")

# numeros = [28,10,9,7,85,6]
# for numero in numeros:
#     if numero%2 == 0:
#         print(f"El numero {numero} es par")
#     else:
#         print(f"El numero {numero} no es par")
        
# data = [
#     [1, 1, 1, 1, 1],
#     [2, 1, 2, 4, 8],
#     [3, 1, 3, 9, 27],
#     [4, 1, 4, 16, 64],
#     [5, 1, 5, 25, 125]
# ]

# for fila in data:
#     print(' '.join(map(str,fila)))

# numeros = [1,2,3,4,5]
# cuadrado_numeros = []

# for numero in numeros:
#     cuadrado_numeros.append(numero ** 2)
# print(cuadrado_numeros)    

# # Hacemos ahora lo mismo con map
# numeros = [1,2,3,4,8]
# cuadrado_numeros = map(lambda x: x ** 2, numeros)
# print(list(cuadrado_numeros))

def cuadrado(numero):
    numero = numero ** 2
    return numero
    
numeros = [5,8,9,4,2.5]
for numero in numeros:
    n_cuadrado = cuadrado(numero)
    print(f"El cuadrado de {numero} es: {n_cuadrado}")

# ## PARA LEERLO SERIA numeros_al_cuadrado = un mapeo con la funcion cuadrado sobre el numero que le pases,,,,,con este objeto podemos ahora rellenar la lista
# numeros_al_cuadrado = map(cuadrado,numeros)
# numeros_al_cuadrado = list(numeros_al_cuadrado)
# print(f"Los numeros al cuadrado son : {numeros_al_cuadrado}")



    



