import pytest
from aircraft import Aircraft, Airbus, Boeing
from passenger import Passenger
from flight import Flight

def test_creacion_objetos_flight():
    """
    Prueba la creación de objetos Flight.
    """
    f1 = Flight(number="BA117", aircraft=Aircraft(registration="G-EUAH", model="Airbus A319", num_rows=22, num_seats_per_row=6))
    assert f1.get_number() == "BA117"
    assert f1.get_aircraft_model() == "Airbus A319"

    f2 = Flight(number="AF92", aircraft=Boeing(registration="F-GSPS", airline="Emirates"))
    assert f2.get_number() == "AF92"
    assert f2.get_aircraft_model() == "Boeing (Emirates)"

    f3 = Flight(number="BA148", aircraft=Airbus(registration="G-EUPT", variant="A319-100"))
    assert f3.get_number() == "BA148"
    assert f3.get_aircraft_model() == "Airbus A319-100"

    # Test inválido
    # f4 = Flight(number="BA14548", aircraft=Airbus(registration="G-EBADMUPT", variant="A3194353-100132"))
    # assert f4.get_number() == "BA141238"
    # assert f4.get_aircraft_model() == "Airbuqdsas A311239-101230"

def test_allocate_passenger():
    """
    Prueba la asignación de pasajeros a los asientos.
    """
    f1 = Flight(number="BA117", aircraft=Aircraft(registration="G-EUAH", model="Airbus A319", num_rows=22, num_seats_per_row=6))
    p1 = Passenger("Jack", "Shephard", "85994003S")
    f1.allocate_passenger("12A", p1.passenger_data())
    assert f1._Flight__seating["12A"] == p1.passenger_data()

    # Test inválido
    # f1.allocate_passenger("12A", p1.passenger_data())
    # assert f1._Flight__seating["12A"] == ("Invalid", "Data", "12345678")

def test_reallocate_passenger():
    """
    Prueba la reasignación de pasajeros a diferentes asientos.
    """
    f1 = Flight(number="BA117", aircraft=Aircraft(registration="G-EUAH", model="Airbus A319", num_rows=22, num_seats_per_row=6))
    p1 = Passenger("Jack", "Shephard", "85994003S")
    f1.allocate_passenger("12A", p1.passenger_data())
    f1.reallocate_passenger("12A", "15F")
    assert f1._Flight__seating["12A"] is None
    assert f1._Flight__seating["15F"] == p1.passenger_data()

    # Test inválido
    # f1.reallocate_passenger("12A", "15F")
    # assert f1._Flight__seating["12A"] == p1.passenger_data()

def test_num_available_seats():
    """
    Prueba el número de asientos disponibles.
    """
    f1 = Flight(number="BA117", aircraft=Aircraft(registration="G-EUAH", model="Airbus A319", num_rows=22, num_seats_per_row=6))
    assert f1.num_available_seats() == 22 * 6
    p1 = Passenger("Jack", "Shephard", "85994003S")
    f1.allocate_passenger("12A", p1.passenger_data())
    assert f1.num_available_seats() == 22 * 6 - 1

    # Test inválido
    # f1.allocate_passenger("12A", p1.passenger_data())
    # assert f1.num_available_seats() == 22 * 6

def test_parse_seat():
    """
    Prueba la conversión de asientos.
    """
    f1 = Flight(number="BA117", aircraft=Aircraft(registration="G-EUAH", model="Airbus A319", num_rows=22, num_seats_per_row=6))
    assert f1._Flight__parse_seat("12A") == (12, "A")
    assert f1._Flight__parse_seat("15F") == (15, "F")

    # Test inválido
    # assert f1._Flight__parse_seat("12A") == (13, "B")

def test_print_seating():
    """
    Prueba la impresión de los asientos.
    """
    f1 = Flight(number="BA117", aircraft=Aircraft(registration="G-EUAH", model="Airbus A319", num_rows=22, num_seats_per_row=6))
    p1 = Passenger("Jack", "Shephard", "85994003S")
    f1.allocate_passenger("12A", p1.passenger_data())
    f1.print_seating()

    # Test inválido
    # f1.allocate_passenger("12A", p1.passenger_data())
    # f1.print_seating()

def test_print_boarding_cards():
    """
    Prueba la impresión de las tarjetas de embarque.
    """
    f1 = Flight(number="BA117", aircraft=Aircraft(registration="G-EUAH", model="Airbus A319", num_rows=22, num_seats_per_row=6))
    p1 = Passenger("Jack", "Shephard", "85994003S")
    f1.allocate_passenger("12A", p1.passenger_data())
    f1.print_boarding_cards()

    # Test inválido
    # f1.allocate_passenger("12A", p1.passenger_data())
    # f1.print_boarding_cards()

def test_invalid_flight_number():
    """
    Prueba la validación del número de vuelo.
    """
    with pytest.raises(ValueError):
        Flight(number="117BA", aircraft=Aircraft(registration="G-EUAH", model="Airbus A319", num_rows=22, num_seats_per_row=6))

    # Test inválido
    # with pytest.raises(ValueError):
    #     Flight(number="BA117", aircraft=Aircraft(registration="G-EUAH", model="Airbus A319", num_rows=22, num_seats_per_row=6))

def test_invalid_seat_allocation():
    """
    Prueba la asignación de un asiento inválido.
    """
    f1 = Flight(number="BA117", aircraft=Aircraft(registration="G-EUAH", model="Airbus A319", num_rows=22, num_seats_per_row=6))
    p1 = Passenger("Jack", "Shephard", "85994003S")
    with pytest.raises(ValueError):
        f1.allocate_passenger("30A", p1.passenger_data())

    # Test inválido
    # with pytest.raises(ValueError):
    #     f1.allocate_passenger("12A", p1.passenger_data())

def test_reallocate_to_occupied_seat():
    """
    Prueba la reasignación a un asiento ocupado.
    """
    f1 = Flight(number="BA117", aircraft=Aircraft(registration="G-EUAH", model="Airbus A319", num_rows=22, num_seats_per_row=6))
    p1 = Passenger("Jack", "Shephard", "85994003S")
    p2 = Passenger("Kate", "Austen", "12589756P")
    f1.allocate_passenger("12A", p1.passenger_data())
    f1.allocate_passenger("15F", p2.passenger_data())
    with pytest.raises(ValueError):
        f1.reallocate_passenger("12A", "15F")

    # Test inválido
    # with pytest.raises(ValueError):
    #     f1.reallocate_passenger("12A", "16F")

if __name__ == "__main__":
    pytest.main()
