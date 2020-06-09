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
        if new_plane == "A320":
            self.plane = "A320"
            self.capacity = 150
        elif new_plane == "A321":
            self.plane = "A321"
            self.capacity = 200
        elif new_plane == "B-787":
            self.plane = "B-787"
            self.capacity = 300
        elif new_plane.lower() == "space shuttle":
            self.plane = "Space Shuttle"
            self.capacity = 7

    def show_report(self):
        report = vars(self)
        for key, value in report.items():
            if key != "manifest":
                print(key.capitalize(), ": ", value)

    def append_manifest(self, person):
        self.manifest.append(person)

    def show_manifest(self):
        print(f"\nManifest for personnel on flight {self.flight}: ")
        for person in self.manifest:
            print(vars(person))


pioneer = Flight('Pioneer', '0800', 'Paris', '1h20', 'A320', 150)
taurus = Flight('Taurus', '0815', 'Munich', '1h50', 'A321', 200)
achilles = Flight('Achilles', '0820', 'Dusseldorf', '1h35', 'A320', 150)