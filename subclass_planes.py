from class_airport import *

class Plane(Airport):
    def __init__(self, plane_model, airline, flight_no, capacity):
        self.plane_model = plane_model
        self.airline_name = airline
        self.__flight_no = flight_no
        self.capacity = capacity

    def get_flight_no(self):
        return self.__flight_no

    def set_flight_no(self):
        return self.__flight_no
