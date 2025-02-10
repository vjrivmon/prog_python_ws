# CLASES Y OBJETOS
class Persona:
    # Atributos de la clase
    def __init__(self, nombre, edad): # Método inicializador, se ejecutará lo primero de la clase
        self.__nombre = nombre # __nombre es un atributo privado, no se puede acceder desde fuera de la clase
        self.__edad = edad 
        # Todos los metodos de la propia clase deben llevar el self como primer parámetro. self.persona, self.edad, etc.
    # Método dentro de la clase
    def mostrar(self): # el self hace referencia al propio objeto, siempre hay que añadirlo al crear un método
        print("Hola " + self.__nombre) # el self hace referencia a los propios atributos de la clase
    def get_nombre(self):
        return self.__nombre

print ("Hola desde persona")
