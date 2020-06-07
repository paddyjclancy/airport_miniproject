# from class_flights import *
#
#
# class FlightReport(Flight):
#
#     def __init__(self, flight, departure, destination, flight_time, plane, capacity):
#         super().__init__(flight, departure)
#         self.destination = destination.capitalize()
#         self.flight_time = flight_time
#         self.plane = plane.capitalize()
#         self.capacity = capacity
#
#
#     def delay(self, new_time):
#         self.departure = new_time
#
#     def divert(self, new_destination):
#         self.destination = new_destination
#
#     def alter_aircraft(self, new_plane):
#         self.plane = new_plane
#
#     def show_report(self):
#         report = vars(self)
#         for key, value in report.items():
#             print(key.capitalize(), ": ", value)
#
#
# pioneer = FlightReport('Pioneer', '0800', 'Paris', '1h20m', 'A321', 300)
