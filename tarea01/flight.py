from aircraft import *
from passenger import *
from pprint import pprint

class Flight:
    def __init__(self, number, aircraft):
        self.__number = number
        self.__aircraft = aircraft
        rows, seats = self.__aircraft.seating_plan()
        self.__seating = {f"{row}{seat}": None for row in rows for seat in seats}
    
    def get_number(self):
        """Obtains the number of the flight
        Returns:
            number: The number of the flight such as 'BA758'
        """
        number = self.__number
        return (number)
    
    def get_aircraft_model(self):
        """Obtains the model of the aircraft
        Returns:
            model: The model of the aircraft such as 'Airbus A319'
        """
        model = self.__aircraft.get_model()
        return (model)
    
    def allocate_passenger(self, seat, passenger):
        """Allocate a seat to a passenger
        Args:
            seat: A seat designator such as '12C' or '21F'
            passenger: The passenger data such as ('Jack', 'Shephard', '85994003S')
        """
        if self.__seating[seat] is not None:
            raise ValueError(f"Seat {seat} already occupied")
        self.__seating[seat] = passenger
    
    def reallocate_passenger(self, from_seat, to_seat):
        """Reallocate a passenger to a different seat
        Args:
            from_seat: The existing seat designator for the passenger such as '12C'
            to_seat: The new seat designator
        """
        if self.__seating[from_seat] is None:
            raise ValueError(f"No passenger to reallocate in seat {from_seat}")
        if self.__seating[to_seat] is not None:
            raise ValueError(f"Seat {to_seat} already occupied")
        self.__seating[to_seat] = self.__seating[from_seat]
        self.__seating[from_seat] = None
    
    def num_available_seats(self):
        """Obtains the amount of unoccupied seats
        Returns:
            The number of unoccupied seats  
        """
        return sum(1 for seat in self.__seating if seat is None)
        
    def print_seating(self):
        """Prints in console the seating plan
        Example of one row:
            {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None}
        """
        pprint(self.__seating)

    def print_boarding_cards(self):
        """Prints in console the boarding card for each passenger
        Example of one boarding card:
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
        """Divide a seat designator in row and letter
            Args:
                seat: The seat designator to be divided such as '12C'
            Returns:
                row: The row of the seat such as 12
                letter: The letter of the seat such as 'C'
        """
        row_numbers, seat_letters = self.__aircraft.seating_plan()
        letter = seat[-1]
        row = int(seat[:-1])
        if row not in row_numbers:
            raise ValueError(f"Invalid row number {row}")
        if letter not in seat_letters:
            raise ValueError(f"Invalid seat letter {letter}")
        return (row, letter)

    def __passenger_seats(self):
        """A generator function to iterate the occupied seating locations
        Returns:
            generator: Tuple of the passenger data and the seat
        """
        for seat, passenger in self.__seating.items():
            if passenger is not None:
                yield (passenger, seat)

