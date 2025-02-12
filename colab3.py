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

# TUPLAS
# Son colecciones de datos ordenadas e inmutables
# Se definen con paréntesis
# Se pueden acceder a los elementos de una tupla mediante el índice
tupla = (1, 2, 3, 4, 5)
print(tupla)
print(tupla[0])
valor = tupla[1] + tupla[2]
print(valor)
# Los métodos que coinciden con las listas son: count(), index() y len()
# Para inicializar una tupla con un único valor:
tupla = (1,)
print(tupla)

# Podemos devolver varios valores en una función
def operaciones(a, b):
    suma = a + b
    resta = a - b
    return suma, resta
a = 5
b = 3
resultado = operaciones(a, b)
print("Suma:", resultado[0], "Resta:", resultado[1])

# DICCIONARIOS
# Son un ejemplo de estructura donde almacenamos datos en pares clave-valor.
# El valor es propiamente el dato que forma parte de la colección, mientras que la clave es un identificador único que nos permite acceder a dicho valor.
# Como los valores de un diccionario no están ordenados, no podemos acceder a ellos mediante un índice, sino que lo hacemos mediante la clave.
# Es similar a una lista, pero en lugar de usar índices, usamos claves para acceder a los elementos. 
# Ejemplo de claves: numeros de teléfono, DNI o dirección de correo.
# Se declara con la palabra reservada dict() o con llaves {}
dic1 = {}
dic2 = dict()
dic = {"nombre": "Pepe", "edad": 25, "ciudad": "Valencia"}
print(dic)
# Los pares clave-valor se encuentran separados por comas y la clave y el valor por dos puntos.
# A la izquierda queda la clave y a la derecha el valor.
dic = {11: 42.1, "usuario2": 33, (1,3,4): "valor3"}
print(dic)

# Operaciones dentro de un Diccionario:
# Para acceder a un valor, se hace mediante la clave
dic = {456: "Pepe", "edad": 25, "ciudad": "Valencia"}
print(dic[456])

# Obtener el tamaño de un diccionario
print(len(dic))

# Comprobar si una clave existe en un diccionario
res = "nombre" in dic
print("¿Existe la clave 'nombre'?", res)

# También podemos almacenar nuevos pares clave-valor en un diccionario empleando la misma sintaxis que empleamos para el acceso a valores.
# Utilizamos la misma sintaxis para insertar un nuevo dato como también para sobreescribir valores asociados a claves ya empleadas en el diccionario
d = { 'usuario1': 23, 'usuario7': 10, 'usuario2' : 4 }
d['usuario3'] = 15
d["usuario1"] = 0 
print(d) 

dic = {123: "Juan", 456: "Maria", 789: "Pedro", "sdfas": 344}

# Añadir / Modificar un elemento
dic[122] = "Eva" #si no existe lo añade
dic["sdfas"] = 345 #si existe lo modifica
print("Modifico clave 'sdfas' y añado la 122: ",dic)

#Otra forma de añadir/modificar el valor de una clave
dic.update({123: "Laura", 456: "Carlos"})
print("Modifico clave 123 y 456: ",dic)

# Eliminar un elemento por su clave
del dic[123]

#Otra forma mediante la que nos podemos guardar el valor eliminado
valor = dic.pop(456)
print("Elimino clave 123 y guardo el valor de la clave 456: ",dic, valor)

# Eliminar todo el diccionario y la variable
#del dic
# Eliminar todos los datos pero mantener la variable
dic.clear()
print("Elimino el diccionario: ",dic)

# Recorrar las claves que tenemos en un Diccionario
dic = {123: "Juan", 456: "Maria", 789: "Pedro", "sdfas": 344}

# Recorrer un diccionario
print("Recorremos un diccionario:")
for i in dic:
    print("Clave: ",i," Valor: ",dic[i])

# Otra forma de recorrerlo un diccionario
print("\nOtra forma de recorrerlo:")
for i in dic.keys():
  print("Clave: ",i," Valor: ",dic[i])

# Recorrer los valores de un Diccionario
print("\nRecorremos los valores de un diccionario:")
for i in dic.values():
    print(i)

#Otra forma de recorrer en dos variables
print("\nPor claves y valores:")
for k, v in dic.items():
    print("Clave: ",k," Valor: ",v)

# También puedes utilizar una comprehension sobre un diccionario. 
# Lo único que cambia con respecto a listas es que tienes que definir la clave.

# Ejemplo de comprehension con aquellos items mayores que 100
dic = {"first": 20, "second": 556, "third": 212, "fourth": 89}

nuevo_dic = {i : dic[i] for i in dic.keys() if dic[i] > 100}
print(nuevo_dic)

# Funciones para utilizar con diccionarios
'''

    clear() Vacía un diccionario eliminando toads las claves y valores.
    copy() Devuelve una copia del diccionario.
    fromkeys() Devuelve una nueva copia del diccionario pero solo con unas claves concretas.
    get() Devuelve el valor de una clave concreta, o None si no existe.
    items() Devuelve una lista de items como una tupla para cada par de clave-valor.
    keys() Devuelve una lista de todas las claves.
    pop() Elimina el item que tenga una clave determinada y lo guarda e una variable.
    popitem() Elimina el último par de clave-valor.
    update() Modifica el valor de una clave determinada, o lo añade si no existe.
    values() Devuelve una lista de todos los valores.

'''

# Multiples valores en un diccionario
persona = {
    "nombre": "Pepe",
    "edad": 25,
    "ciudad": "Valencia",
    "email": "paco@gmail.com"
}

#La forma de acceder a los datos de una persona sería así:
print(persona["nombre"])
print(persona["edad"])
print(persona["ciudad"])
print(persona["email"])

# Podemos tener una clave asociada a cada persona

persona = {
    "nombre" : "Paco",
    "fecha" : "02/04/1980",
    "poblacion" : "Valencia"
}

persona2 = {
    "nombre" : "Ana",
    "fecha" : "22/10/1985",
    "poblacion" : "Gandia"
}


dic = { 123: persona, 456: persona2 }
print(dic)

# EJERCICIOS

# 1. Escribe una función que reciba dos diccionarios con claves de tipo string y valores de tipo numérico, 
# y que devuelva un nuevo diccionario que contenga los dos anteriores. Muestra el resultado por pantalla.

def nuevo_diccionario(dic1, dic2):
    dic3 = dic1.copy()
    dic3.update(dic2)
    return dic3

dic1 = {"hola": 1, "adios": 2, "como": 3, "estás": 4, "yo": 5}
dic2 = {"muy": 6, "bien": 7, "y": 8, "tu": 9, "que": 10, "tal": 11, "?": 12}

resultado = nuevo_diccionario(dic1, dic2)
print(resultado)

# 2. Escribe una función que reciba un diccionario y una lista de palabras. 
# La función debe devolver un nuevo diccionario con los items del diccionario 
# cuyas claves correspondan a alguna de las palabras de la lista. 
# Muestra el resultado por pantalla.

def coincidencia(dic, lista):
    dic2 = {k: dic[k] for k in lista if k in dic}
    return dic2

dic = {"Hola": 123, "adios": 9, "pues": 1, "muy": 9, "bien": 3}
lista = ["Hola", "me", "llamo", "Vicente", "y", "estoy", "muy", "bien"]
res = coincidencia(dic, lista)
print(res)

# 3. Escribe un programa que lea un texto por teclado. 
# Posteriormente debe crear un diccionario donde las claves sean las palabras del texto 
# y sus valores el número de apariciones de cada una de éstas en el texto. Muestra el resultado por pantalla.

# Leer el texto del usuario
texto = input("Introduce tu texto: ")

# Función para contar las apariciones de cada palabra
def contar_palabras(texto):
    palabras = texto.split()  # Dividir el texto en palabras
    diccionario = {}
    for palabra in palabras:
        if palabra in diccionario:
            diccionario[palabra] += 1  # Incrementar el contador si la palabra ya está en el diccionario
        else:
            diccionario[palabra] = 1  # Añadir la palabra al diccionario con un contador de 1
    return diccionario

# Contar las palabras en el texto
resultado = contar_palabras(texto)

# Mostrar el resultado por pantalla
print(resultado)
        
# 4. Escribe una función que reciba un diccionario de valores numéricos y devuelva el valor mínimo de este diccionario. 
# Muestra el resultado por pantalla.
def valor_minimo(dic):
    dic2 = dic.values()
    minimo = next(iter(dic2))  # Inicializar con el primer valor del diccionario
    for i in dic2:
        if i < minimo:
            minimo = i
    print("El valor minimo en tu diccionario es: ",minimo)
    return minimo

dic = {"1": 1, "5": 8, "4": 7, "90": 12}
res = valor_minimo(dic)

# 5. Escribe una función que reciba el siguiente diccionario y cuente la cantidad de items que tienen True el campo success:

def items(dic):
    contador = 0
    for key in dic:
        if dic[key]['success'] == True:
            contador += 1
    print("Número de veces que aparece True: ", contador)
    return contador

dic = {
 1 : {'id': 1, 'success': True, 'name': 'Lary'},
 2 : {'id': 2, 'success': False, 'name': 'Rabi'},
 3 : {'id': 3, 'success': True, 'name': 'Alex'}
}

res = items(dic)


# Iteradores y Generadores
#r ecorremos un string
palabra = "hola"
for i in palabra:
  print(i)

#recorremos una lista
lista = [2, 5, 8, 0, 11]
for i in lista:
  print(i)

#recorremos un diccionario
dic = {123: "Juan", 456: "Maria", 789: "Pedro"}
for i in dic:
  print(i)

# Podemos usar la función iter() para obtener un iterador de un objeto iterable
lista = [2, 5, 8, 0, 11]

#obtenemos un iterator sobre la lista
iterador = iter(lista)

#utilizamos next cada vez que queremos el siguiente dato del iterador
print("Ahora me hace falta un dato")
print(next(iterador))
print("Ahora me hace falta otro")
print(next(iterador))
print("Ahora otro")
print(next(iterador))

# Una función generadora es una función que devuelve un objeto generador en lugar de una secuencia de valores
# Cada vez que se le pasa como parametro a la función next(), se ejecuta hasta que se encuentra con la palabra reservada yield
# Para construir una función generadora, simplemente tenemos que utilizar yield en vez de return, pero el resto del código es similar. 
#Función generadora de números pares
def numeros():
  i = 0
  #bucle infinito
  while True:
    yield i
    i+=2

#La función generadora nos devuelve un generador
generador = numeros()

#utilizamos next cada vez que queremos generar un nuevo dato
print("Ahora me hace falta un dato")
print(next(generador))
print("Ahora me hace falta otro")
print(next(generador))
print("Ahora otro")
print(next(generador))

# Cuando llamamos a next la primera vez, la función se ejecuta hasta encontrar el yield, 
# que devuelve el valor indicado y que congelará la ejecución de la función hasta la próxima vez que pidamos un nuevo valor.

#Función generadora de números pares
def numeros():
  print("NUMEROS: inicio de la función")
  i = 0
  #bucle infinito
  while True:
    print("NUMEROS: antes del yield")
    yield i
    print("NUMEROS: después del yield")
    i+=2

#La función generadora nos devuelve un generador
generador = numeros()
print("Después de llamar a la función y obtener el generador")

#utilizamos next cada vez que queremos generar un nuevo dato
print("Ahora me hace falta un dato")
print(next(generador))
print("Ahora me hace falta otro")
print(next(generador))
print("Ahora otro")
print(next(generador))

# EJERCICIOS

# Fibonacci
# Escribe una función generadora de la secuencia de Fibonacci y comprueba su correcto funcionamiento. 
# Los valores de esta secuencia se calculan siguiendo la siguiente fórmula:

def fibo():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
        
generador = fibo()
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))

# Nueva Función Generadora
def suma_tiempos(inicio, fin, incremento):
    """Función que devuelve tuplas de tiempo (hh,mm,ss) desde una hora inicial hasta una hora final
    Args: 
        inicio (hh,mm,ss): Hora inicial
        fin (hh,mm,ss): Hora final
        incremento (segundos): Incremento en segundos
    Returns: 
        hora (hh,mm,ss): Tupla de tiempo
    """
    h, m, s = inicio
    h_fin, m_fin, s_fin = fin

    while (h, m, s) <= (h_fin, m_fin, s_fin):
        yield (h, m, s)
        s += incremento
        m += s // 60
        s = s % 60
        h += m // 60
        m = m % 60

# Ejemplo de uso
inicio = (2, 12, 36)
fin = (2, 14, 0)
incremento = 3600

generador = suma_tiempos(inicio, fin, incremento)
for tiempo in generador:
    print(tiempo)


