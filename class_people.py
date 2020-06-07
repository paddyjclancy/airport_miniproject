from class_airport import *


class People(Airport):

    def __init__(self, full_name, dob, nationality):
        self.__name = full_name
        self.__dob = dob
        self.nationality = nationality

    def get_full_name(self):
        return self.__name

    def set_full_name(self, new_name):
        self.__name = new_name
        return f"Name overridden to:  {self.__name}"

    def get_dob(self):
        return self.__dob

    def set_dob(self, new_dob):
        self.__dob = new_dob
        return "DOB for {self.__name} overridden to:  {self.__dob}"

    def get_nationality(self):
        return self.nationality

    def set_nationality(self, new_nation):
        self.nationality = new_nation
        return "Nationality for {self.__name} overridden to:  {self.nationality}"
