class Passenger:
    def __init__(self, name, surname, id_card):
        self.__name = name
        self.__surname = surname
        self.__id_card = id_card

    
    def passenger_data(self):
        """Obtains the data of a passenger
        Returns:
            name: The passenger's name such as 'Jack'
            surname: The passenger's family name such as 'Shephard'
            id_card: The passenger's id card such as '85994003S'
        """
        nombre = self.__name
        apellidos = self.__surname
        dni = self.__id_card
        return (nombre, apellidos , dni)
        