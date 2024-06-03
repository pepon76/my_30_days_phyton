#### EJERCICICOS CON DICCIONARIOS
# Acceder a un elemento por nombre de clave genera un error si la clave no existe. Para evitar este error, primero debemos verificar si existe una clave o podemos usar el método get. El método get devuelve None, que es un tipo de datos de objeto NoneType, si la clave no existe.

# persona = {
#     "nombre" :     "Jose",
#     "apellidos":   "Moreno",
#     "edad":        45,
#     "lenguajes":   {"html","css","R","python"}
# }

# print(persona.get("nombre"))
# print(persona["nombre"])

# print("nombre" in persona)

# pop(key): removes the item with the specified key name:
# popitem(): removes the last item
# del: removes an item with specified key name

# The items() method changes dictionary to a list of tuples.
# print(persona.items())

# The keys() method gives us all the keys of a a dictionary as a list.
# print(persona.keys())
# print(persona.values())

# ### EJERCICIOS

# Escribe una función contar_palabras que reciba una cadena de texto y devuelva un diccionario donde las claves sean las palabras y los valores sean el número de veces que aparece cada palabra en el texto.
# def contar_palabras(cadena):
#     frecuencias = {}
#     #Separamos la palabras de la cadena creando una lista llamada palabras
#     palabras = cadena.split()    
#     # recorremos la lista palabras   
#     for palabra in palabras:
#         if palabra in frecuencias:
#             frecuencias[palabra] += 1
#         else:
#             frecuencias[palabra] = 1
#     return frecuencias

# print(contar_palabras("Esta es una cadena de prueba es solo una prueba"))

# Ejercicio 2: Traductor simple
# Escribe una función traducir que reciba un diccionario con pares de palabras (inglés-español) y una lista de palabras en inglés. La función debe devolver una lista con la traducción de las palabras, utilizando el diccionario. Si una palabra no se encuentra en el diccionario, debe mantenerse en inglés.
# def traducir(diccionario,palabras):
#      # creamos la lista de palabras traducidas vacia
#     traducciones = []
#     # recorremos la lista palabras, verificando si tiene traduccion
#     for palabra in palabras:
#         if palabra in diccionario:
#             traducciones.append(diccionario[palabra])
#         else:
#             traducciones.append(palabra)
#     return traducciones
        
# # Probamos el codigo
# diccionario = {"hello": "hola", "world": "mundo", "python": "pitón"}
# palabras = ["hello", "world", "python", "rocks"]
# print(traducir(diccionario,palabras))

# # Ejercicio 3: Mezcla de diccionarios
# # Escribe una función mezclar_diccionarios que reciba dos diccionarios y los combine en uno solo. Si hay claves repetidas, los valores deben sumarse (si son numéricos) o concatenarse (si son cadenas).  

# def mezclar_diccionarios(dic1,dic2):
#     combinado = dic1.copy()
    
    # Recorrer cada clave y valor en el segundo diccionario
#     for clave,valor in dic2.items():
#         if clave in combinado:
#             if isinstance(valor,(int,float)) and isinstance(combinado[clave],(int,float)):
#                 combinado[clave] += valor
#             elif isinstance(valor,(str)) and isinstance(combinado[clave], str):
#                 combinado[clave] += f" {valor}"
#         else:
#             combinado[clave] = valor
#     return combinado
                
# dic1 = {'a': 1, 'b': 2, 'c': 'hello'}
# dic2 = {'b': 3, 'c': 'world', 'd': 4}

# print(mezclar_diccionarios(dic1,dic2))

# Ejercicio 4: Invertir un diccionario
# Escribe una función invertir_diccionario que reciba un diccionario y devuelva un nuevo diccionario donde las claves sean los valores y los valores sean las claves del diccionario original. Si hay valores duplicados, uno de ellos se pierde.

# def invertir_diccionario(dic):
#     dic_invertido = {}
#     for clave,valor in dic.items():
#         dic_invertido[valor] = clave
#     return dic_invertido

# dic = {'a': 1, 'b': 2, 'c': 3}
# print(invertir_diccionario(dic))


# Escribe una función fusionar_listas que reciba dos listas de igual longitud, una con claves y otra con valores, y devuelva un diccionario donde los elementos de la primera lista sean las claves y los elementos de la segunda lista sean los valores.
    
# def fusionar_listas(clave,valor):
#     resultado = {}
#     for clave,valor in zip(clave,valor):
#         resultado[clave] = valor
#     return(resultado)
    
# claves = ['nombre', 'edad', 'ciudad']
# valores = ['Ana', 25, 'Madrid']

# print(fusionar_listas(claves,valores))

def suma_valores_dic(dic):
    valores = []
    for clave,valor in dic.items():
        valores.append(valor)
    return sum(valores)
        
 
print(suma_valores_dic({"item1":5,"item2":7,"item3":13}))

        
    
