from aircraft import *
from passenger import *
from pprint import pprint
import math

class Flight:
    """
    Representación de un vuelo.

    Atributos:
        number (str): El número del vuelo. Se suele representar como: 'BA758'.
        aircraft (Aircraft): La aeronave asignada al vuelo. Boeing / Airbus.
        seating (dict): El plan de asientos para el número de filas y asientos por fila del vuelo.
    """

    def __init__(self, number, aircraft):
        """
        Inicializa un vuelo con su número y la aeronave asignada.

        Args:
            number (str): El número del vuelo.
            aircraft (Aircraft): La aeronave asignada al vuelo.
        """
        self.__number = number
        self.__aircraft = aircraft
        rows, seats = self.__aircraft.seating_plan()
        self.__seating = {f"{row}{seat}": None for row in rows for seat in seats}
    
    def get_number(self):
        """
        Obtiene el número del vuelo.

        Returns:
            str: El número del vuelo.
        """
        number = self.__number
        return (number)
    
    def get_aircraft_model(self):
        """
        Obtiene el modelo del avión.

        Returns:
            str: El modelo del avión.
        """
        model = self.__aircraft.get_model()
        if isinstance(self.__aircraft, Airbus):
            model += f" {self.__aircraft.get_variant()}"
        elif isinstance(self.__aircraft, Boeing):
            model += f" ({self.__aircraft.get_airline()})"
        return (model)
    
    def allocate_passenger(self, seat, passenger):
        """
        Asigna un asiento a un pasajero.

        Args:
            seat (str): Un ejemplo de asiento es '12C' o '21F'.
            passenger (tuple): Datos de ejemplo de un pasajero ('Jack', 'Shephard', '85994003S').
        """
        if self.__seating[seat] is not None:
            raise ValueError(f"El asiento {seat} está ya ocupado")
        self.__seating[seat] = passenger
    
    def reallocate_passenger(self, from_seat, to_seat):
        """
        Reasigna un pasajero a un asiento diferente.

        Args:
            from_seat (str): El diseñador de asiento existente para el pasajero como '12C'.
            to_seat (str): El nuevo diseñador de asiento.
        """
        if self.__seating[from_seat] is None:
            raise ValueError(f"Ningún pasajero recolocado en el asiento {from_seat}")
        if self.__seating[to_seat] is not None:
            raise ValueError(f"El asiento {to_seat} está ocupado")
        self.__seating[to_seat] = self.__seating[from_seat]
        self.__seating[from_seat] = None
    
    def num_available_seats(self):
        """
        Obtiene la cantidad de asientos libres.

        Returns:
            int: El número de asientos libres.
        """
        return sum(1 for seat in self.__seating if seat is None)
        
    def print_seating(self):
        """
        Imprime por consola el plan de asientos.

        Ejemplo de una fila:
            {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None}
        """
        pprint(self.__seating)

    def print_boarding_cards(self):
        """
        Imprime en consola la tarjeta de embarque para cada pasajero.

        Ejemplo de una tarjeta de embarque:
        ----------------------------------------------------------
        |     Jack Sheppard 85994003S 15E BA758 Airbus A319      |
        ----------------------------------------------------------
        """
        for seat, passenger in sorted(self.__seating.items()):
            if passenger is not None:
                print(f"----------------------------------------------------------")
                print(f"|     {passenger[0]} {passenger[1]} {passenger[2]} {seat} {self.__number} {self.__aircraft.get_model()}      |")
                print(f"----------------------------------------------------------")

    def __parse_seat(self, seat):
        """
        Divide un diseñador de asiento en fila y letra.

        Args:
            seat (str): Un ejemplo de lo que debe de dividir el parseador de asientos: '12C'.

        Returns:
            tuple: Una tupla que contiene la fila (int)(12) y la letra (str)(C) del asiento.
        """
        row_numbers, seat_letters = self.__aircraft.seating_plan()
        letter = seat[-1]
        row = int(seat[:-1])
        if row not in row_numbers:
            raise ValueError(f"Número de fila inválida {row}")
        if letter not in seat_letters:
            raise ValueError(f"Letra de asiento inválida {letter}")
        return (row, letter)

    def __passenger_seats(self):
        """
        Una función generadora para iterar las ubicaciones de asientos ocupados.

        Returns:
            generator: Tupla de los datos del pasajero y el asiento.
        """
        for seat, passenger in self.__seating.items():
            if passenger is not None:
                yield (passenger, seat)

