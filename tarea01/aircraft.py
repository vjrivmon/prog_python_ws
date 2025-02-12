from passenger import * 
import math

class Aircraft:
    """
    Representación de una aeronave.

    Atributos:
        registration (str): La matrícula de la aeronave.
        model (str): El modelo de la aeronave.
        num_rows (int): El número de filas en la aeronave.
        num_seats_per_row (int): El número de asientos por fila.
    """

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        """
        Inicializa una aeronave con su matrícula, modelo, número de filas y número de asientos por fila.

        Args:
            registration (str): La matrícula de la aeronave.
            model (str): El modelo de la aeronave.
            num_rows (int): El número de filas en la aeronave.
            num_seats_per_row (int): El número de asientos por fila.
        """
        self.__registration = registration
        self.__model = model
        self.__num_rows = num_rows
        self.__num_seats_per_row = num_seats_per_row

    def get_registration(self):
        """
        Obtiene la matrícula de la aeronave.

        Returns:
            str: La matrícula de la aeronave.
        """
        registration = self.__registration
        return (registration)
    
    def get_model(self):
        """
        Obtiene el modelo de la aeronave.

        Returns:
            str: El modelo de la aeronave.
        """
        model = self.__model
        return (model)
    
    def seating_plan(self):
        """
        Genera un plan de asientos para el número de filas y asientos por fila.

        Returns:
            tuple: Una tupla que contiene una lista de números de fila y una cadena de letras de asientos.
        """
        rows = list(range(1, self.__num_rows + 1))
        seats = "ABCDEF"
        return (rows, seats)

    def get_num_rows(self):
        """
        Obtiene el número de filas en la aeronave.

        Returns:
            int: El número de filas.
        """
        return self.__num_rows
    
    def num_seats(self):
        """
        Calcula el número de asientos en la aeronave.

        Returns:
            int: El número de asientos.
        """
        seats = self.__num_rows * self.__num_seats_per_row
        return (seats)

class Airbus(Aircraft):
    """
    Representación de un avión modelo Airbus.

    Atributos:
        variant (str): La variante del Airbus.
    """

    def __init__(self, registration, variant, model="Airbus", num_rows=22, num_seats_per_row=6):
        """
        Inicializa un Airbus con su matrícula, variante, modelo, número de filas y número de asientos por fila.

        Args:
            registration (str): La matrícula del Airbus.
            variant (str): La variante del Airbus.
            model (str): El modelo del Airbus. Por defecto es "Airbus".
            num_rows (int): El número de filas en el Airbus. Por defecto es 22.
            num_seats_per_row (int): El número de asientos por fila en el Airbus. Por defecto es 6.
        """
        super().__init__(registration, model, num_rows, num_seats_per_row)
        self.__variant = variant
    
    def get_variant(self):
        """
        Obtiene la variante del tipo de avión del Airbus.

        Returns:
            str: La variante del tipo de avión del Airbus.
        """
        variant = self.__variant
        return (variant)
    
class Boeing(Aircraft):
    """
    Representación de un avión con el modelo Boeing.

    Atributos:
        airline (str): La aerolínea del modelo Boeing.
    """

    def __init__(self, registration, airline, model="Boeing", num_rows=30, num_seats_per_row=9):
        """
        Inicializa un Boeing con su matrícula, aerolínea, modelo, número de filas y número de asientos por fila.

        Args:
            registration (str): La matrícula del Boeing.
            airline (str): La aerolínea del Boeing.
            model (str): El modelo del Boeing. Por defecto es "Boeing".
            num_rows (int): El número de filas en el Boeing. Por defecto es 30.
            num_seats_per_row (int): El número de asientos por fila en el Boeing. Por defecto es 9.
        """
        super().__init__(registration, model, num_rows, num_seats_per_row)
        self.__airline = airline
    
    def get_airline(self):
        """
        Obtiene la aerolínea del Boeing.

        Returns:
            str: La aerolínea del Boeing.
        """
        airline = self.__airline
        return (airline)