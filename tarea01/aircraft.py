from passenger import * 

class Aircraft:
    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self.__registration = registration
        self.__model = model
        self.__num_rows = num_rows
        self.__num_seats_per_row = num_seats_per_row

    def get_registration(self):
        """Obtains the registration of the aircraft
        Returns:
            registration: The registration of the aircraft such as 'E-MYTA'
        """
        registration = self.__registration
        return (registration)
    
    def get_model(self):
        """Obtains the model of the aircraft
        Returns:
            model: The model of the aircraft such as 'Boeing 747'
        """
        model = self.__model
        return (model)
    
    def seating_plan(self):
        """Generates a seating plan for the number of rows and seats per row
        Returns:
            rows: A list of row numbers.
            seats: A string of letters such as "ABCDEF"
        """
        rows = list(range(1, self.__num_rows + 1))
        seats = "ABCDEF"
        return (rows, seats)

    def get_num_rows(self):
        """Obtains the number of rows in the aircraft
        Returns:
            num_rows: The number of rows
        """
        return self.__num_rows
    
    def num_seats(self):
        """Calculates the number of seats
        Returns:
            seats: The number of seats
        """
        seats = self.__num_rows * self.__num_seats_per_row
        return (seats)

class Airbus(Aircraft):
    def __init__(self, registration, variant, model="Airbus", num_rows=22, num_seats_per_row=6):
        super().__init__(registration, model, num_rows, num_seats_per_row)
        self.__variant = variant
    
    def get_variant(self):
        """Obtains the variant of the aircraft
        Returns:
            variant: The variant of the aircraft such as 'A319-100'
        """
        variant = self.__variant
        return (variant)
    
class Boeing(Aircraft):
    def __init__(self, registration, airline, model="Boeing", num_rows=30, num_seats_per_row=9):
        super().__init__(registration, model, num_rows, num_seats_per_row)
        self.__airline = airline
    
    def get_airline(self):
        """Obtains the airline of the aircraft
        Returns:
            airline: The airline of the aircraft such as 'Emirates'
        """
        airline = self.__airline
        return (airline)