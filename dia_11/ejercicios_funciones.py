### FUNCIONES ####

# Exercises: Level 1
# Declare a function add_two_numbers. It takes two parameters and it returns a sum.

# def add_two_numbers(num1,num2):
#     sum = num1 + num2
#     return(sum)

# print(add_two_numbers(500,20))

# from math import pi

# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
# def area_of_circle(radio):
#     area = pi * radio**2
#     return(area)
   
    
# print(round(area_of_circle(20),2))

# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
# def add_all_nums(*nums):
#     total = 0
#     for i in nums:
#         if isinstance(i,int):
#             total += i
#         else:
#             print("Revisa los argumentos y asegurate de que todos tienen que ser numeros")
#             return(None)
#     return(total)

# print(add_all_nums(15,58,69,74,78,100))

# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

# def convert_celsius_to_fahrenheit(celcius):
#     far = (celcius * 9/5) + 32
#     return(far)
    
# print(convert_celsius_to_fahrenheit(85))

# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

# autum = {"septiembre","octubre","noviembre"}
# winter = {"diciembre","enero","febrero"}
# spring = {"marzo","abril","mayo"}
# summer = {"junio","julio","agosto"}

# def check_season(mes):
#     mes = mes.lower()
#     if mes in autum:
#         print("Otoño")
#     elif mes in winter:
#         print("Invierno")
#     elif mes in spring:
#         print("Primavera")
#     elif mes in summer:
#         print("Verano")
#     else:
#         print("Revisa la ortografia,el mes que has escrito parece no existir")
        
# check_season("JULios")

# Write a function called calculate_slope which return the slope of a linear equation
        
# def calculate_slope(punto1,punto2):
#     x1,y1 = punto1
#     x2,y2 = punto2
#     if x2-x1 == 0:
#         print("Pendiente indefinida, no se puede dividir por 0")
#     else:
#         pendiente = (y2-y1)/(x2-x1)
#         return(pendiente)
    
# punto1 = (1,2)
# punto2 = (3,6)

# print(calculate_slope(punto1,punto2))

# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.

def print_list(lista):
    for i in lista:
        print(i)

mi_lista = ["UNo","DOS", 3, 78]

print_list(mi_lista)
    