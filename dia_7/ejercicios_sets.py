# #### EJERCICICOS CON SETS
# frutas = {'banana', 'orange', 'mango', 'lemon'}

# # for i in frutas:
# #     print(i)

# # print("banana" in frutas)

# # frutas.add("cherry")
# # print(frutas)

# # frutas.update(["cherry","cebolla","pepino","castaña"])
# # print(frutas.pop())
# # print(frutas)

# # # syntax
# # st1 = {'item1', 'item2', 'item3', 'item4'}
# # st2 = {'item5', 'item6', 'item7', 'item8'}
# # st1.update(st2) # st2 contents are added to st1
# # print(st1)

# st1 = {'item1','item4'}
# st2 = {'item2', 'item3'}
# print(st2.difference(st1))
# print(st1.difference(st2))
# print(st1.isdisjoint(st2))

# Ejercicio 1: Creación y Acceso Básico
# Crea un conjunto llamado frutas con los elementos "manzana", "pera", "plátano".
# Agrega la fruta "cereza" al conjunto frutas.
# Intenta agregar la fruta "manzana" nuevamente y observa qué sucede.
# Elimina la fruta "pera" del conjunto.

# frutas = {"manzana", "pera", "plátano"}
# print(frutas)
# frutas.add("cereza")
# print(frutas)
# frutas.add("manzana")
# print(frutas)
# frutas.remove("pera")
# print(frutas)

# Ejercicio 2: Operaciones de Conjuntos
# Crea dos conjuntos: conjunto1 = {1, 2, 3, 4} y conjunto2 = {3, 4, 5, 6}.
# Encuentra la intersección de conjunto1 y conjunto2.
# Encuentra la unión de conjunto1 y conjunto2.
# Encuentra la diferencia de conjunto1 y conjunto2 (elementos que están en conjunto1 pero no en conjunto2).
# Encuentra la diferencia simétrica de conjunto1 y conjunto2 (elementos que están en uno de los conjuntos pero no en ambos).

conjunto1 = {1, 2, 3, 4}
conjunto2 = {3, 4, 5, 6}

print(conjunto1.intersection(conjunto2))
print(conjunto1.union(conjunto2))
print(conjunto1.difference(conjunto2))
print(conjunto1.symmetric_difference(conjunto2))

# Ejercicio 3: Verificar Pertenencia y Subconjuntos
# Crea un conjunto llamado numeros con los elementos {10, 20, 30, 40, 50}.
# Verifica si el número 30 está en el conjunto numeros.
# Verifica si el número 60 está en el conjunto numeros.
# Crea otro conjunto subconjunto = {20, 30} y verifica si subconjunto es un subconjunto de numeros.
numeros = {10, 20, 30, 40, 50}
print({30}.issubset(numeros))
print({60}.issubset(numeros))
subconjunto = {20, 30}
print(subconjunto.issubset(numeros))

# Ejercicio 4: Modificación de Conjuntos
# Crea un conjunto llamado animales con los elementos "gato", "perro", "ratón".
# Utiliza el método update para agregar los elementos "elefante", "león", "tigre" al conjunto animales.
# Utiliza el método discard para eliminar "ratón" del conjunto animales.
# Utiliza el método pop para eliminar y obtener un elemento aleatorio del conjunto animales.

animales = {"gato","perro","ratón"}
animales.update(["elefante", "león", "tigre"])
print(animales)
animales.discard("ratón")
print(animales)
print(f"El animal eliminado del conjunto animales es: {animales.pop()}")
print(animales)


# Ejercicio 5: Operaciones Avanzadas con Conjuntos
# Crea un conjunto llamado a con los elementos {1, 2, 3, 4, 5}.
# Crea otro conjunto llamado b con los elementos {4, 5, 6, 7, 8}.
# Usa el método issubset para verificar si a es un subconjunto de b.
# Usa el método issuperset para verificar si a es un superconjunto de {1, 2}.
# Usa el método isdisjoint para verificar si a y {6, 7} son conjuntos disjuntos (no tienen elementos en común).
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a.issubset(b))
print(a.issuperset({1,2}))
print(a.isdisjoint({6,7}))

# Ejercicio 6: Conversiones y Comparaciones
# Crea una lista de números con elementos repetidos: lista = [1, 2, 2, 3, 4, 4, 5].
# Convierte la lista a un conjunto para eliminar duplicados.
# Convierte el conjunto de nuevo a una lista.
# Compara dos conjuntos: conjuntoA = {1, 2, 3} y conjuntoB = {3, 2, 1} para ver si son iguales.
lista = [1, 2, 2, 3, 4, 4, 5]
print(lista)
unicos = set(lista)
lista = unicos
print(lista)

conjuntoA = {1, 2, 3} 
conjuntoB = {3, 2, 1}
print(conjuntoA.isdisjoint(conjuntoB))