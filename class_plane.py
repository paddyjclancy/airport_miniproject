from class_airport import *

class Plane(Airport):
    def __init__(self, plane_model, airline, flight_no, capacity):
        self.plane_model = plane_model
        self.airline_name = airline
        self.__flight_no = flight_no
        self.capacity = capacity

    def get_flight_no(self):
        return self.__flight_no

    def set_flight_no(self, new_no):
        self.__flight_no = new_no
        print(f"Flight number allocated to plane:  {self.plane_model} updated to: {self.__flight_no}")


airbus0 = Plane("A320", "BA", 10000, 150)
airbus1 = Plane("A320", "BA", 10001, 150)
airbus2 = Plane("A320", "BA", 10002, 150)
airbus3 = Plane("A321", "BA", 10003, 200)
airbus4 = Plane("A321", "BA", 10004, 200)
airbus5 = Plane("A321", "BA", 10005, 200)
airbus6 = Plane("A321", "BA", 10006, 200)
boeing0 = Plane("B-787", "BA", 10500, 300)
boeing1 = Plane("B-787", "BA", 10501, 300)
boeing2 = Plane("B-787", "BA", 10502, 300)
