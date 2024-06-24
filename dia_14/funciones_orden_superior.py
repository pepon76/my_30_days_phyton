def suma_1(numero):
  return numero + 1

def cuadrado(numero):
    return numero ** 2


def suma(num1,num2,f):
    return f(num1 + num2)

print(suma(10,5,suma_1))
print(suma(10,5,cuadrado))

## Built-in Higher Order Functions
# map
lista = [2,4,8,9]
print(list(map(cuadrado,lista)))
print(list(map(lambda x:x**3,lista)))

#filter
# def mayor(x):
#     if x>5:
#         return True

def mayor(x):
    return x>5
    
print(list(filter(mayor,lista)))
print(list(filter(lambda x: x>5,lista)))

#reduce

from functools import reduce
def eleva(num1,num2):
    return num1 ** num2

print(reduce(eleva,lista))