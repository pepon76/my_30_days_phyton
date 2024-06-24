# mi_lista = [35,24,62,52,30,30,17]

# mi_lista_2 = [i**2 for i in mi_lista]
# print(mi_lista_2)



# def cuadrado(x):
#     return x**2

# otra_lista = [cuadrado(i) for i in range(9)]
# print(f"ESta es mi otra_lista: {otra_lista}")

# otra_lista_2 = [cuadrado(i) for i in range(9) if i < 5]
# print(f"ESta es mi otra_lista_2: {otra_lista_2}")


# def fizzbuzz():
#     for i in range(1,101):
#         if i%3 == 0 and i%5 == 0:
#             print("fizzbuzz")
#         elif i%3 == 0:
#             print("fizz")
#         elif i%5 == 0:
#             print("buzz")
#         else:
#             print(i)
            
# fizzbuzz()


# def anagrama(text1,text2):
#     if text1.lower() == text2[::-1].lower():
#         print("ES ANAGRAMA")
#     else:
#         print("NO ES ANAGRAMA")
        
# anagrama("amor","Roma")



# def fibo(longitud):
#     numero_a = 0
#     numero_b = 1
#     lista = []
#     while len(lista) < longitud:
#         lista.append(numero_a)
#         numero_a, numero_b = numero_b, numero_a + numero_b
#     print(f"La serie de fibonacci con longitud {longitud} es: \n{lista}")
    
# fibo(15)

def impares(numero):
    i = 0
    while i <= numero:
        if i % 2 != 0:
            print(i)
        i += 1
impares(100)
            

        
         
    

        


