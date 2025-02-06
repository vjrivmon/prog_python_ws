# FICHEROS

f = open("fichero.txt", mode="r", encoding="utf-8")

res = f.read()
print(res)

# Para trabajar con ficheros CSV
import csv
with open('ejemplo.csv', mode='r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
# el reader te guarda el contenido del fichero en una lista de listas

