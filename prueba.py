x = 10
print("-----------------Fin del bucle-----------------")
print(x)

"Bucle"

x = 1

while x <= 10:
    print(x)
    x += 1
print("-----------------Fin del bucle-----------------")
for i in range(1, 11):
    print(i)
print("-----------------Fin del bucle-----------------")
for i in "ana", "juan", "luis", 10:
    print(i)
print("-----------------Fin del bucle-----------------")

# Creamos una lista
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# ELementos ordenados, cada uno tendrá un posición
print(type(lista))
#Indexación
print(lista[2:4])
# Recorrer una lista
for i in lista:
    print(i)

for i in range(len(lista)):
    print(lista)