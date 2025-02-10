# FUNCIONES, TUPLAS y DICCIONARIOS

# FUNCIONES
# Se crean funciones con la finalidad de reutilizar o hacer más eficiente el código
# Se definen con la palabra reservada "def" seguida del nombre de la función y los parámetros

# Ejemplo de función

def media(lista_numeros):
    suma = 0
    for n in lista_numeros:
        suma = suma + n
    return suma / len(lista_numeros)

# -------- MAIN --------
num = [1, 5, 3, 2]
resultado = media(num)
print("La media de la lista es: ",str(resultado))

# Otro ejemplo de función
def saludar(nombre = "Pepe"):
    return "Hola " + nombre

# -------- MAIN --------
res = saludar()
print(res)

# Último ejemplo de función
def saludar(edad, nombre = "Pepe"):
    return "Hola " + nombre + ", tienes " + str(edad) + " años"

# -------- MAIN --------
res = saludar(25)
print(res)

# KWARGS (Keyword Arguments) --> Nos permite variar el orden en el que están definidos los parámetros
def saludar(edad, nombre = "Pepe"):
    return "Hola " + nombre + ", tienes " + str(edad) + " años"

# -------- MAIN --------
res = saludar(nombre = "Juan", edad = 25)
print(res)

# Podemos pasar un número variable de argumentos a una función. Para ello, se utiliza el operador *args
def ordenar(*args):
  lista = list(args) #creamos una lista con los valores recibidos
  lista.sort()
  print(lista)

# -------- MAIN --------
ordenar(5, 2, 7, 4)
ordenar(7, 2, 8, 6, 3, 1, 5)

# Funciones LAMBDA --> Funciones anónimas que se pueden utilizar para realizar operaciones sencillas
# Sintaxis: lambda argumentos: expresión
# argumentos: parámetros de la función
# expresión: lógica que se va a realizar
# Un ejemplo de este tipo de funciones es cuando lo que queremos que haga la función es una simple línea. Se puede evitar el def:
# Ejemplo:
res = lambda x, y : x * y
print(res(5, 2))
# En la función de arriba, x e y son los parámetros de entrada, mientras que x * y es la expresión que se evalúa y retorna el resultado

# EJERCIOS
# Crea una función llamada without_first_letter que dada una lista de palabras, devuelva una nueva lista con la primera letra de cada palabra eliminada.

def without_first_letter(palabras):
    nueva_lista = [palabra[1:] for palabra in palabras]
    return nueva_lista

# -------- MAIN --------
palabras = ["Pepe", "Carlos", "Emilio", "Ratón", "Levante"]
res = without_first_letter(palabras)
print(res)

# Crea una función llamada get_minimum que dado una lista de números,devuelva el valor mínimo encontrado el dicho array.
def get_minimum(numeros):
    minimo = numeros[0]
    for i in numeros:
        if i < minimo:
            minimo = i
    print(minimo)
    return minimo

# -------- MAIN --------
numeros = [4, 9, 0, 1, 3]
get_minimum(numeros)

# Crea una función llamada every_element_greater_than que tome por parámetro un número y una lista numérica 
# y devuelva True si todos los elementos son mayores que el número pasado por parámetro y False en caso contrario.

def every_element_greater_than(numero, lista):
    for i in lista:
        if numero <= i:
            print("Tu número no es mayor a todos los elementos de la lista")
            return False
    print("Tu número es mayor a todos los elementos de la lista")
    return True

# -------- MAIN --------
numero = 2
lista = [2, 1, 0, 3]
resultado = every_element_greater_than(numero, lista)
print("Resultado:", resultado)

# Crea una función llamada greater_than_average que tome un parámetro x de tipo numérico, 
# y una lista llamada data_array. La función deberá devolver cierto en caso de que el valor x sea mayor que la media de la lista, y falso en caso contrario.

def greather_than_average(x, data_array):
    suma = 0
    for i in data_array:
        suma = suma + i
    media = suma / len(data_array)
    if x > media:
        print("True")
        return True
    else: 
        print("False")
        return False

# -------- MAIN --------
x = 7
data_array=[3, 5, 8, 9]
greather_than_average(x, data_array)

# Crea una función llamada clean_list que tome una lista de nombres de usuarios 
# y una lista de nombres de usuarios baneados y devuelva una nueva lista con los usuarios no baneados.

def clean_list(limpios, baneados):
    lista = []
    for usuario in limpios:
        if usuario not in baneados:
            lista.append(usuario)
    print(lista)
    return lista

# -------- MAIN --------
limpios = ["Alberto", "Cesar", "Mariano", "Victor"]
baneados = ["Cesar", "Victor"]
clean_list(limpios, baneados)

# COMPREHENSIONS
# Son una forma de crear listas, diccionarios y conjuntos de forma más eficiente y legible
# Son una forma elegante de definir y crear listas basándonos en otras listas
# Imagina que queremos crear una lista que multiplique por dos los elementos de otra lista. 
# Esto lo podríamos hacer de varias maneras: 
# (1) de manera tradicional iterando la lista con un bucle
# (2) utilizando una función map(), pero también 
# (3) con una comprehension. 
# Observa el siguiente ejemplo que produce el mismo resultado de las 3 maneras:

valores = [2, 5, 12, 10]

# (1) Manera tradicional
resultado = []
for i in valores:
  resultado.append(i * 2)
print(resultado)

# (2) Ejemplo con map
resultado = map(lambda i : i * 2, valores)
print(list(resultado))

# (3) Ejemplo con comprehension
resultado = [i * 2 for i in valores]
print(resultado)

# Sintaxis de una comprehension
# nueva_lista = [expression for item in list]
# expression: operación que se va a realizar
# item: elemento de la lista
# list: lista de elementos

# Así nos podemos quedar con los pares y mayores que 10
lista = [14, 5, 12, 16, 9, 7, 10]

nueva = [x for x in lista if x % 2 == 0 if x > 10]
print(nueva)

# También if y else
lista = [14, 5, 12, 16, 9, 7, 10]

nueva = [ x if x % 2 == 0 else 0 for x in lista ]
print(nueva)

# Una comprehension puede transformarse en un bucle, pero no yodos los bucles pueden transformarse en una comprehension

# EJERCICIOS

# Crea una función llamada squares_greater que dada una lista de números, 
# devuelva una nueva lista con los cuadrados de aquellos números mayores que 10.
lista = [5, 9, 13, 3, 20, 57, 33, 11]
nueva = [x*x for x in lista if x >10]
print(nueva)

# Crea una función llamada word_length que dada una lista de palabras, 
# devuelva una nueva lista con la longitud de cada una siempre y cuando la palabra no sea "el".
lista = ["el", "macaco", "de", "tu", "pito"]
nueva = [x if x == "el" else len(x) for x in lista]
print(nueva)

# Crea una función llamada clean_list que tome una lista de nombres de usuarios 
# y una lista de nombres de usuarios baneados y devuelva una nueva lista con los usuarios no baneados.
limpios = ["Yilun", "Pablo", "Mimi", "Irene", "Vicente"]
baneados = ["Yilun", "Pablo"]
nueva = [x for x in limpios if x not in baneados]
print(nueva)
