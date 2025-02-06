# Tipos de valores

# int    | valor numérico de tipo entero                  | x = 23
# float  | valor numérico de tipo coma flotante o decimal | x = 11.34
# string | valor de tipo cadena de texto                  | x1 = "Hola", x2 = 'Hola'
# bool   | valor de tipo booleano                         | a = True, b = False

# Se puede hacer un casting para convertir un tipo de dato en otro.
# Ejemplo: Casting de string a int
y = 3.5
print(int(y))
print(int("345"))

# Operaciones Aritméticas

# + | Suma de 2 valores                                                     | a = 1 + 23, b = a + 33
# - | Resta de 2 vaores                                                     | a = 23 - 1
# * | Multiplicación de 2 valores                                           | a = 2 * 3
# / | División decimal de 2 valores. Siempre devuelve un valor decimal      | a = 10 / 2
# //| División entera de 2 valores. Devuelve un valor entero                | a = 10 // 3
# % | Devuelve el resto de la división entre 2 valores                      | a = 10 % 3
# **| Realiza la potenciación de un valor a otro                            | a = 2 ** 3

# GUIA DE ESTILO
# variables en minúsculas y con guiones bajos: unit_price mejor que unitPrice
# constantes en mayúsculas y con guiones bajos: MAX_VALUE
# clases en CamelCase: Product

# ENTRADA / SALIDA
# La función print acepta varios argumentos separados por comas
# Se puede imprimir información por pantalla mediante marcas de inerpolación. {campo.formato}
# Campos: número que identifica el número de argumento que se desea interpolar en la cadena
# Formato: define el formato del argumento a interpolar mediante la siguiente forma donde cada elemento entre corchetes es opcional

x = 5

print("El valor es {0} y si queremos otro valor sería así {1}".format(x, x/3)) #dentro de format ponemos los valores en orden que queremos imprimir
print("El valor es {1} y si queremos otro valor sería así {0}".format(x, x/3)) #podemos cambiar el orden
print("El valor es {0} y si queremos otro valor sería así {a}".format(x, a=x/3)) #... y utilizar variables
print("El valor es {0:.3f} y si queremos otro valor sería así {a:.2f}".format(x, a=x/3)) #... y si queremos formatear los decimales de la salida

# La función input permite leer información desde el teclado. Se almacena el valor introduico en una variabe en formato string
# Ejemplo de input
x = input("Introduce un número: ")
print("El número introducido es: ", x)

# MÓDULOS
# Un módulo es un archivo que contiene código Python. Son archivos que contienen definiciones de funciones y declaraciones ejecutables.
# Debemos de colocar la palabra import seguida del nombre del módulo
# Ejemplo: import math
import math

x = 10
print("La raíz cuadrada de", x, "es", math.sqrt(x))

# Se puede también renombrar el módulo importado
# Ejemplo: import math as m

# Ejercicios

# Realiza un programa que calcule la suma de los números 43582134 y 1234567, 
# almacene el resultado en una variable, e imprima el resultado por pantalla.

x = 43582134
y = 1234567
z = x + y
print(z)

# Hoy en día, la tasa de cambio entre el euro y el dolar es de 0.85 euros por cada dólar. 
# Atendiendo a esta información, construye un programa que lea una cantidad de dólares por teclado e informe al cliente de la cantidad de euros que obtendría al cambiar.
# ERROR: Se debe de convertir a float el input que introduzca el usuario
euros = float(input("Introduce cuanto quieres convertir de euros (€) a dólares ($): "))
dolares = euros * 0.85

print("La cantidad en dólares($) es: ", dolares)

# Se cree comúnmente que 1 año humano equivale a 7 años en un perro. 
# Construye un programa que le pregunte al usuario en qué año nació y le informe de su edad perruna. 
# Asume que el año actual es 2025.
edad = int(input("Introduce tu año de nacimiento: "))
año = 2025
edad_persona = año - edad
edad_perro = edad_persona * 7
print("Si fueras un perro, tu edad sería de: ", edad_perro, "años")

# IF y ELSE
# Python es un lenguaje que no utiliza llaves para separar bloques de código (i.e., {}) sino que se utilizan dos puntos (i.e., :)
# En python es OBLIGATORIA la tabulación para separar bloques de código
# Puedes elegir entre tabular o utilizar 4 espacios en blanco, favorece a que el código sea más legible
# No se deben de mezclar ambos

# Ejemplo de if y else
num = 7

if num >= 5:
  print("El número es mayor o igual a 5")
else:
  print("El número es menor que 5")

print("Esta línea se ejecuta siempre")

# Podemos anidar if y else de la siguiente forma: elif

# OPERACIONES LÓGICAS
# <  | Devuelve True si el primer valor es menor que el segundo valor proporcionado                 | 3 < 2, 1 < 2, a < b
# <= | Devuelve True si el primer valor es menor o igual que el segundo valor proporcionado         | 3 <= 2, 2 <= 2, a <= b
# >  | Devuelve True si el primer valor es mayor que el segundo valor proporcionado                 | 3 > 2, 2 > 1, a > b
# >= | Devuelve True si el primer valor es mayor o igual que el segundo valor proporcionado         | 3 >= 2, 2 >= 2, a >= b
# == | Devuelve True si los dos valores proporcionados son iguales                                  | 3 == 2, 2 == 2, a == b
# != | Devuelve True si los dos valores proporcionados son distintos                                | 3 != 2, 2 != 2, a != b
# and| Devuelve True si ambos valores proporcionados son True                                       | a > b and b > c, 3 < 2 and (3 % 2 == 1), a > b and b < c
# or | Devuelve True si al menos una de las 2 expresiones proporcionadas es True                    | a > b or b > c, 3 < 2 or (3 % 2 == 1), a > b or b < c
# not| Devuelve True si la expresión proporcionada es False                                         | not a > b, not 3 < 2, not (3 % 2 == 1)

# EJERCICIOS

# 1. Implementa un programa que lea la hora en formato 24 horas y lo convierta a formato 12 horas. 
# Como ejemplos de ejecución:
# Introduce la hora: 8
# Introduce los minutos: 57
# Son las 08:57 AM
# Introduce la hora: 21
# Introduce los minutos: 31
# Son las 09:31 PM
# Introduce la hora: 26:
# Hora inválida. Deben ser entre 0 y 23.

hora = int(input("Introduce la hora: "))
minutos = int(input("Introduce los minutos: "))
if hora < 12 and minutos <= 59:
    print("Son las:", hora, ":", minutos, "AM")
elif hora < 24 and minutos <= 59: 
    hora2 = 24 - hora # 24 - 13 = 11
    hora3 = 12 - hora2 # 12 - 11 = 1 
    print("Son las:", hora3, ":", minutos, "PM" )
else:
    if hora >= 24:
        print("Hora inválida. Deben de ser entre 0 y 23")
    if minutos >= 60:
        print("Minutos inválidos. Recuerda que 60 minutos es 1 hora")

# 2 Se nos ha solicitado programar el calculador de la tarifa a pagar por los usuarios de una compañía de telefonía móvil. 
# Todos los usuarios pagan una tarifa base de 10 euros al mes siempre que no hablen más de 180 minutos al mes. 
# A partir de los 180 minutos, los usuarios pagan 10 céntimos por cada minuto hablado desde los 180 hasta los 240 minutos. 
# A partir de ese momento, los usuarios pagan 20 céntimos por cada minuto por cada minuto extra consumido a partir de los 240. 
# El calculador debe pedir al usuario los minutos hablados y devolver los euros a pagar.

minutos_usuario = int(input("Cuantos minutos has hablado por teléfono este mes? "))
if minutos_usuario < 180:
    print("Deberás de pagar 10€ como parte de tu tarifa base")
elif minutos_usuario > 180 and minutos_usuario < 240:
    minutos_extras = 240 - minutos_usuario # 190 minutos --> 240-190=50
    minutos_extras = 10 + minutos_extras * 0.1 # 10 + 5 = 15€
    print("Deberás de abonar esta cantidad: ", minutos_extras, "€")
elif minutos_usuario > 240:
    minutos_extras = minutos_usuario - 240 # 260 minutos --> 260-240=20
    minutos_extras = 10 + minutos_extras * 0.2 # 10 + 4
    print("Deberás de abonar: ", minutos_extras, "€")

# 3 Otra persona y tú queréis reservar mesa en un restaurante. 
# Queremos un programa que nos pregunte el estilo de vestir nuestro y el de nuestro compañero, que serán valores entre 0 y 10. 
# Si uno de los dos tenemos un estilo de 8 o superior, entonces sí que tendremos mesa para cenar y deberá mostrar un mensaje por pantalla. 
# Esto es así siempre y cuando uno de los dos no tenga un 2, en cuyo caso no tendremos mesa. 
# En cualquier otro caso, el mensaje que debe mostrar es que no sabemos si tendremos mesa.

persona1 = int(input("¿Cómo vas vestido hoy? (Valores entre 0 y 10) ")) # persona 1 = 2
persona2 = int(input("¿Cómo vas vestido hoy? (Valores entre 0 y 10) ")) # persona 2 = 10

''''
if persona1 >= 8 or persona2 >= 8:
    print("Tenéis acceso a una mesa esta noche")
else:
    if persona1 == 2 or persona2 == 2:
        print("Lo sentimos, no podemos darte una mesa esta noche") # Debería de imprimir esto por pantalla
    print("No podemos asegurarte una mesa para esta noche")
'''
if persona1 == 2 or persona2 == 2:
    print("Lo sentimos, no podemos darte una mesa esta noche") # Debería de imprimir esto por pantalla
elif persona1 >= 8 or persona2 >= 8:
    print("Tenéis acceso a una mesa esta noche")
else:
    print("No podemos asegurarte una mesa para esta noche")

# 4 Realiza un programa que pregunte por un día de la semana y si estamos o no de vacaciones. 
# El programa deberá mostrar un mensaje indicando a qué hora nos suena la alarma. 
# Entre semana, la alarma sonará a las 8:00 y los fines de semana a las 10:00. 
# Sin embargo, si estamos de vacaciones, los días entre semana sonará a las 10:00 y los fines de semana estará apagada.

dia_de_la_semana = input("¿Que día de la semana es? ")
vacaciones = input("¿Estás de vacaciones? ")

if vacaciones == "SI":
    if dia_de_la_semana == "SABADO" or dia_de_la_semana == "DOMINGO":
        print("No tienes ninguna alarma programada, disfruta del finde :)")
    else:
        print("Como estás de vacaciones, tu alarma está programada a las 10 de la mañana")
elif vacaciones == "NO":
    if dia_de_la_semana == "SABADO" or dia_de_la_semana == "DOMINGO":
        print("La alarma está programada el día", dia_de_la_semana, "a las 10 de la mañana")
    else:
        print("Como no estás de vacaciones, la próxima alarma está programada para el día: ", dia_de_la_semana, "a las 8:00")

# 5 Realiza un programa que pregunte tres valores enteros y muestre un mensaje por pantalla 
# indicando si los dos primeros tienen una diferencia máxima de 1 
# mientras que el tercero tiene una diferencia mayor que 2 con los otros dos. 
# Utiliza la función abs(sum) para calcular el valor absoluto de un número.

numero_1 = int(input("Dime tu primer número: "))
numero_2 = int(input("Dime tu segundo número: "))
numero_3 = int(input("Dime tu tercer número: "))

numero_1 = abs(numero_1) # 2 # 1
numero_2 = abs(numero_2) # 3 # 2
numero_3 = abs(numero_3) # 5 # 3

resta_2_primeros = numero_2 - numero_1 # 3-2=1 #2-1=1
diferencia = numero_3 - resta_2_primeros #5-1=4 4>2 #3-1=2
if resta_2_primeros == 1:
    print("Tus 2 primeros números tienen una diferencia de 1")
    if diferencia > 2:
        print("Se cumplen las 3 condiciones, los 2 primeros tienen una diferencia de 1 y la resta entre ambos es mayor que 2 con el tercero") # Se debe de imprimir esto

# WHILE Y FOR
# Existen 2 tipos de bucles en Python: while y for
# Podemos utilizar while para aquellos casos donde queremos que se repita el bucle mientras se cumpla una condición.
# Ejemplo de while
i = 0
while i < 5:
    print(i)
    i += 1
# El bucle for lo utilizamos cuando sabemos cuántas veces queremos que se repita el bucle.
# La instrucción range(n) nos permite generar una secuencia de números desde 0 hasta n-1.
# Ejemplo de for
for i in range(5):
    print(i)
print("Fin del bucle")

# Esto mismo lo podemos hacer escribiendo los valores que queremos iterar
for i in 1, 2, 3, "casa", "coche", 3.14:
    print(i)
print("Fin del bucle")

# EJERCICIOS
# Realiza un programa para calcular el factorial de un número entero introducido por el teclado.
numero = int(input("Introduce un número: "))
factorial = 1
i = numero
while i > 0:
    factorial = factorial * i
    i = i - 1
print("El factorial de tu número es: ", factorial)

# Implementa un juego que genere un número entero aleatorio entre 1 y 100. 
# Entonces, el usuario deberá introducir números por teclado para intentar adivinar el número generado. 
# Cada vez que el usuario introduzca un número por teclado, el programa deberá determinar si el número es el generado inicialmente (ganando el usuario la partida), 
# si el número introducido por el usuario es múltiplo o divisor del número (informando de que el número introducido es múltiplo o divisor), o si no es ninguno de los otros dos casos. 
# Al final de la partida, el número de puntos obtenido por el usuario es 100 menos el número de intentos del usuario. 
# La puntuación debe imprimirse al final del juego.
import random
numero_aleatorio = random.randint(1, 100)
print(numero_aleatorio)
puntos = 100
numero_usuario = int(input("¿Cuál crees que es el número escogido? "))
while numero_aleatorio != numero_usuario:
    if numero_aleatorio % numero_usuario == 0:
        print("¡FALLASTE! Pero tu número es divisor del número aleatorio")
    elif numero_usuario !=0 and numero_aleatorio % numero_usuario == 0:
        print("¡FALLASTE! Pero tu número es múltiplo del número aleatorio")
    else:
        print("¡LO SENTIMOS! Pero tu número no es ni divisor ni múltiplo del número aleatorio")
    numero_usuario = int(input("Pero no te preocupes, tienes OTRO INTENTO: "))
    puntos = puntos - 1
print("¡ENHORABUENA! Has acabado el juego, tu puntuación final ha sido de:",puntos, "puntos")
        
# Estructuras de datos
# Listas
# Son secuencias de elementos separados por comas. La lista es una estructura que puede crecer o decrecer de forma dinámica según añaadimos o eliminamos elementos.
# En Python, las listas pueden contener elementos de diferentes tipos.
# Creación de listas
datos = [] #lista vacía
datos = list() #lista vacía
datos = [4, "mensaje", -3, 4.5] #lista con 5 elementos
# 2 de las operaciones más comunes: indexing y slicing
# Indexing: acceder a un elemento de la lista mediante su posición (índice)
print(datos[0]) #imprime el primer elemento de la lista
# Podemos modificar un elemento de la lista
datos[1] = "nuevo mensaje"
# Se pueden utilizar índices negativos, donde -1 es el último elemento de la lista, -2 el penúltimo, etc.
print(datos[-1]) #imprime el último elemento de la lista
# Slicing: acceder a un conjunto de elementos de una lista
# Esta operación nos permite trocear una lista en subconjuntos
# Cada operación te devuelve una nueva lista
print(datos[1:3]) #imprime los elementos 1 y 2 de la lista
print(datos[:2]) #imprime los elementos 0 y 1 de la lista
print(datos[2:]) #imprime los elementos 2 y 3 de la lista
# Podemos modificar un conjunto de elementos de la lista
datos[:2] = [1, 2]
# Repetir elementos
datos = [1, 2] * 3 # [1, 2, 1, 2, 1, 2]
# Añadir elementos a una lista
datos.append(4) # [1, 2, 1, 2, 1, 2, 4]
# Podemos utilizar steps para saltarnos algunos elementos en la operación de slicing
datos = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(datos[::2]) # [10, 12, 14, 16, 18]
print(datos[2:7:3]) # [12, 15]
'''
Las listas nos ofrecen varios métodos muy útiles para trabajar con ellas, entre los que destacamos los siguientes:

    len() Devuelve la longitud de la lista.
    append() Añade un elemento al final de la lista.
    clear() Elimina todos los elementos de la lista, dejándola vacía.
    copy() Crea una copia de la lista.
    count() Cuenta cuántas veces aparece un elemento en la lista.
    extend() Añade los elementos de una lista al final de otra.
    index() Devuelve la posición de un elemento dentro de la lista.
    insert() Añade un elemento en una determinada posición de la lista.
    pop() Elimina un elemento de la lista y lo devuelve.
    del() Elimina un elemento de la lista por su posición.
    remove() Elimina un elemento de la lista por su valor.
    reverse() Invierte el orden de elementos de una lista.
    sort() Ordena una lista. Con el parámetro reverse=True especificamos que sea orden inverso.

'''

datos = [4, "mensaje", -15, 3.4]

#Obtener la longitud de una lista
longitud = len(datos)
print(longitud)

#Añadir un elemento al final
datos.append(12)
print("Añado el 12 al final: ", datos)

#Añadir un elemento en una posición determinada (sin machacar el existente)
datos.insert(2,"nuevo_elemento")
print("Añado 'nuevo_elemento' en pos 2: ", datos)

#Buscar un elemento
print("Posición del -15:", datos.index(-15))
print("Está el -15?:", -15 in datos)

#Combinar dos listas
datos.extend([55, 22])
print("Combino dos listas: ", datos)

datos = [4, "mensaje", -15, 3.4]

#Obtener la longitud de una lista
longitud = len(datos)
print(longitud)

#Añadir un elemento al final
datos.append(12)
print("Añado el 12 al final: ", datos)

#Añadir un elemento en una posición determinada (sin machacar el existente)
datos.insert(2,"nuevo_elemento")
print("Añado 'nuevo_elemento' en pos 2: ", datos)

#Buscar un elemento
print("Posición del -15:", datos.index(-15))
print("Está el -15?:", -15 in datos)

#Combinar dos listas
datos.extend([55, 22])
print("Combino dos listas: ", datos)

datos = [4, "mensaje", -15, 3.4]

#Obtener la longitud de una lista
longitud = len(datos)
print(longitud)

#Añadir un elemento al final
datos.append(12)
print("Añado el 12 al final: ", datos)

#Añadir un elemento en una posición determinada (sin machacar el existente)
datos.insert(2,"nuevo_elemento")
print("Añado 'nuevo_elemento' en pos 2: ", datos)

#Buscar un elemento
print("Posición del -15:", datos.index(-15))
print("Está el -15?:", -15 in datos)

#Combinar dos listas
datos.extend([55, 22])
print("Combino dos listas: ", datos)

# Podemos utilizar un bucle FOR para recorrer los elementos de una lista
datos = [4, "mensaje", -15, 3.4]
for i in datos:
    print(i)
# Podemos utilizar la instrucción in para comprobar si un elemento está en la lista (método mucho más cómodo que utilizar un bucle)
if "mensaje" in datos:
    print("mensaje está en la lista")
is_34 = 3.4 in datos
print(is_34)
is_23 = 23 in datos
print(is_23)

# Break nos permite romper el bucle en el momento en el que se cumple una condición
for i in [5, 2, 3, 7, 4, 1, 7]:
  if i == 7:
    print("Encontrado!")
    break

print("Fin")

# Continue nos permite saltar a la siguiente iteración del bucle en el momento en el que se cumple una condición
for i in [5, 2, 3, 7, 4, 1, 7]:
  if i == 7:
    print("Encontrado!")
    continue
  print("Este código sólo se ejecuta si no entra por el if, ya que el continue se carga la iteración")
print("Fin")

# Módulo RANDOM
# nos permite realizar acciones aleatorias como generar números aleatorios, imprimir un valor de una lista, etc.
import random
  
#imprimimos un valor aleatorio
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(random.choice(lista))

#barajamos una lista
random.shuffle(lista)
print(lista)

#creamos un entero aleatorio entre 1 y 4 (ambos incluidos)
res = random.randint(1, 4)
print(res)
