import math
class Passenger:
    """
    Representación de un pasajero.

    Atributos:
        name (str): El nombre del pasajero.
        surname (str): El apellido del pasajero.
        id_card (str): El documento de identidad (DNI) del pasajero.
    """

    def __init__(self, name, surname, id_card):
        """
        Inicializa un pasajero con su nombre, apellido y documento de identidad.

        Args:
            name (str): El nombre del pasajero.
            surname (str): El apellido del pasajero.
            id_card (str): El documento de identidad del pasajero.
        """
        self.__name = name
        self.__surname = surname
        self.__id_card = id_card

    def passenger_data(self):
        """
        Obtiene los datos de un pasajero.

        Returns:
            tuple: Una tupla que contiene el nombre, apellido y documento de identidad del pasajero.
        """
        nombre = self.__name
        apellidos = self.__surname
        dni = self.__id_card
        return (nombre, apellidos , dni)
