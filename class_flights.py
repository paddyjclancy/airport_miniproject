from class_airport import *

# Parent Class = Flight()
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
        self.Flight = flight.capitalize()
        self.Departure = departure
        Flight.instances.append(self.Flight)
