# Day 2: 30 Days of python programming'

################################ LEVEL 1 #########################################################

# Declare a first name variable and assign a value to it
first_name = "Jose Francisco"
# Declare a last name variable and assign a value to it
last_name = "Moreno de la Rosa"
# Declare a full name variable and assign a value to it
full_name = first_name + " " + last_name
# Declare a country variable and assign a value to it
country = "España"
# Declare a city variable and assign a value to it
city = "Malaga"
# Declare an age variable and assign a value to it
age = 45
# Declare a year variable and assign a value to it
year = 1976
# Declare a variable is_married and assign a value to it
is_married = True
# Declare a variable is_true and assign a value to it
is_true = True
# Declare a variable is_light_on and assign a value to it
is_light_on = False
# Declare multiple variable on one line
nombre,apellidos,edad = "Jose","Moreno",45


################################ LEVEL 2 #########################################################

# Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(nombre))
print(type(apellidos))
print(type(edad))
# Using the len() built-in function, find the length of your first name
print(len(first_name))
# Compare the length of your first name and your last name
print(len(first_name) == len(last_name)  )
# Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4
# Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
print(total)
# Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
print(diff)
# Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two
print(product)
# Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
print(division)
# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_one % num_two
print(remainder)
# Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
print(exp)
# Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
print(floor_division)
# The radius of a circle is 30 meters.
radius = float(input("Introduce el radio del circulo a calcular:"))
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
import math
area_of_circle = math.pi * radius **2
print(f"El area del circulo es : {area_of_circle} metros cuadrados")
# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2 * math.pi * radius
print(f"La circunferencia del circulo es : {circum_of_circle} metros")
# Take radius as user input and calculate the area.
# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
nombre_usuario = input("Introduzca su nombre: ")
apellido_usuario = input("Introduzca sus apellidos: ")
pais_usuario = input("Introduzca su pais de nacimiento: ")
edad = int(input("Introduzca su edad: "))

# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help("keywords")
