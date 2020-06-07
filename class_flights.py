from class_airport import *

# Parent Class = flight()
#
# Sub Classes = FlightReport(), AttendeeReport(), Cities(), Planes()
# ME    # FlightReport() -
# ME    # AttendeeReport() -
        # Cities() - destination, distance
        # Planes() - model, capacity, cruising_speed

# Pseudo
# TDD
# Code


class Flight(Airport):
    instances = []

    def __init__(self, flight, departure):
        self.flight = flight.capitalize()
        self.departure = departure
        Flight.instances.append(self.flight)
