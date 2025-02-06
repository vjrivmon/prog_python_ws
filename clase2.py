# Orden de aparición de los elementos: 1
print("Hola mundo")
# Tuplas 2
def saludar(nombre) :
    return "Hola " + nombre

# ------ MAIN ------
res = saludar("Vicente")
print(res)

# Lambda 3
def elevar_a_2(x):
    return x ** 2
res = elevar_a_2(5)
print(res)

# Lamda con funciones 4
# Funcion al vuelo
res = lambda x: x ** 2
print(res(5)) # se guarda esta variable, que le pasas este valor por paréntesis

# Listas de números 5

lista = [4, 5, 1, 3, 8, 2]

lista2 = []

for i in lista:
    lista2.append(i ** 2) 
print(lista2)

# Comprehension de listas 6
lista3 = [i ** 3 for i in lista] # Se mete todo entre corchetes
print(lista3)

lista4 = [i ** 3 for i in lista if i % 2 == 0] # Se mete todo entre corchetes y numeros pares
print(lista4)

# TUPLAS
tupla = (1, 2, 3, 4, 5) # va entre paréntesis en lugar de corchetes como una lista
print(tupla[2]) 
# El objeto tupla no soporta la asignación, son inmutables (no se pueden modificar)
def elevar_a_2(x,y):
    return x ** x, y ** y
res1, res2 = elevar_a_2(5, 3)
print(res1)

# DICCIONARIOS
# Es un json, donde hay claves y valores
# Lista elementos ordenados
# Tuplas elementos ordenados
# Diccionarios elementos desordenados

diccionario1 = { "usuario1": "Ana", "usuario2": "Juan", "usuario3": "Luis" }
print(diccionario1["usuario1"])

diccionario2 = { "usuario1": 
                { "nombre": "Juan", "edad": 25},
                "usuario2": 
                { "nombre": "Ana", "edad": 30},
                "usuario3": 
                { "nombre": "Luis", "edad": 35}
}
print("--------------")
print(diccionario2["usuario1"]["nombre"])
for i in diccionario2.keys():
    print(i)