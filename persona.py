from colab5 import Persona

# --------------- MAIN ---------------
p = Persona("Pepe", 25)
p.mostrar()

# En python los paramteros son publicos, por eso se puede acceder a ellos directamente
print(p.get_nombre())