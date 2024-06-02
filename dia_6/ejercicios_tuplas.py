#### EJERCICICOS CON TUPLAS
# Ejercicio 1: Crear y acceder a tuplas
# Crea una tupla con los siguientes elementos: 1, 2, 3, "a", "b", "c".
# Accede al primer y al último elemento de la tupla.
# Intenta modificar el tercer elemento de la tupla y observa qué sucede.

mi_tupla = (1, 2, 3, "a", "b", "c")
print(mi_tupla[0])
print(mi_tupla[-1])
# mi_tupla[2] = 5

# Ejercicio 2: Operaciones básicas con tuplas
# Crea dos tuplas: tupla1 = (1, 2, 3) y tupla2 = (4, 5, 6).
# Concátalas en una nueva tupla tupla3.
# Multiplica tupla1 por 3.

tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla3 = tupla1 + tupla2
print(tupla3)
print(tupla1 * 3)

# Ejercicio 3: Desempaquetar tuplas
# Crea una tupla con los valores: ("John", "Doe", 25).
# Desempaqueta la tupla en variables nombre, apellido y edad.
# Imprime las variables para verificar que se han desempaquetado correctamente.

tupla5 = ("John", "Doe", 25)
nombre,apellidos,edad = tupla5
print(f"El nomre es: {nombre}\nEl apellido es: {apellidos}\nLa edad es: {edad}")

# Ejercicio 4: Tuplas y bucles
# Crea una tupla con varios elementos: (1, 3, 5, 7, 9, 11).
# Utiliza un bucle for para iterar sobre la tupla e imprimir cada elemento.
tupla6 = (1, 3, 5, 7, 9, 11)
for i in tupla6:
    print(i)
    
# Ejercicio 5: Funciones y tuplas
# Escribe una función que reciba una tupla de números y devuelva la suma de todos sus elementos.
# Prueba la función con una tupla de ejemplo (10, 20, 30, 40).

def imprime_tupla(tupla):
     print(tupla)
imprime_tupla((10, 20, 30, 40))

# Ejercicio 6: Tuplas y listas
# Crea una lista de tuplas, donde cada tupla contiene el nombre y la edad de una persona: [("Ana", 30), ("Luis", 25), ("Maria", 22)].
# Itera sobre la lista de tuplas e imprime el nombre y la edad de cada persona.
n = 1
lista1 = [("Ana", 30), ("Luis", 25), ("Maria", 22)]
for i in lista1:     
    print(f"PERSONA_{n}-->Nombre:{i[0]}\t\tEdad:{i[1]}")
    n = n+1
  
# Ejercicio 7: Comparación de tuplas
# Crea dos tuplas: tupla1 = (1, 2, 3) y tupla2 = (1, 2, 4).
# Compara las tuplas usando los operadores de comparación (==, !=, <, >) y explica el resultado de cada comparación.
tupla1 = (1, 2, 3)
tupla2 = (1, 2, 4)
print( tupla1 == tupla2)
print( tupla1 != tupla2)
print( tupla1 < tupla2)
print( tupla1 > tupla2)

# Ejercicio 8: Uso de la función zip
# Crea dos listas: nombres = ["Ana", "Luis", "Maria"] y edades = [30, 25, 22].
# Utiliza la función zip para combinar estas listas en una lista de tuplas.
# Itera sobre la lista de tuplas e imprime cada tupla.

nombres = ["Ana", "Luis", "Maria"]
edades = [30, 25, 22]
combinada = list(zip(nombres,edades))
for i in combinada:
    print(i)
    
# Ejercicio 9: Contando elementos
# Crea una tupla con elementos repetidos: (1, 2, 3, 1, 2, 1, 4, 1).
# Usa el método count para contar cuántas veces aparece el número 1 en la tupla.
repetidos = (1, 2, 3, 1, 2, 1, 4, 1)
print(repetidos.count(1))

# Ejercicio 10: Índices y subtuplas
# Crea una tupla: (10, 20, 30, 40, 50).
# Usa el método index para encontrar la posición del elemento 30.
# Extrae una subtutla con los primeros tres elementos.
tupla7 = (10, 20, 30, 40, 50)
print(tupla7.index(30))
subtupla7 = tupla7[0:3]
print(subtupla7)
