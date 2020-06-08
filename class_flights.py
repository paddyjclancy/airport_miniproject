from class_airport import *


class Flight(Airport):
    instances = []

    def __init__(self, flight, departure, destination, flight_time, plane, capacity, manifest=None):
        self.flight = flight.capitalize()
        self.departure = departure
        Flight.instances.append(self.flight)
        self.destination = destination.capitalize()
        self.flight_time = flight_time
        self.plane = plane.capitalize()
        self.capacity = capacity
        self.manifest = manifest
        if manifest is None:
            self.manifest = []

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

    def append_manifest(self, passenger):
        self.manifest.append(passenger)

    def show_manifest(self):
        print(f"\nManifest for personnel on flight {self.flight}: ")
        for person in self.manifest:
            print(vars(person))


