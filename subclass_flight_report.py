from class_flights import *


class FlightReport(Flight):

    def __init__(self, flight, departure, destination, distance, plane, capacity):
        self.flight = flight.capitalize()
        self.departure = departure
#       self.eta = eta
        self.destination = destination.capitalize()
#       self.distance = distance
        self.plane = plane.capitalize()
#       self.capacity = capacity

    def delay(self, new_time):
        self.departure = new_time

    def divert(self, new_destination):
        self.destination = new_destination

    def alter_aircraft(self, new_plane):
        self.plane = new_plane

    def show_report(self):
        report = vars(self)
        for key, value in report.items():
            print(key.capitalize(), ": ", value)
