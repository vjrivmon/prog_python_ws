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
        if i <= numero:
            print("Tu numero no es mayor a los que hay en la lista")
            return False  
    return True

# -------- MAIN --------
numero = 6
lista = [2, 1, 0, 3]
every_element_greater_than(numero, lista)