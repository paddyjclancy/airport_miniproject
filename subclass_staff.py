from class_people import *


class Staff(People):

    def __init__(self, full_name, airline, title, dob, tax_no, nationality):
        super().__init__(full_name, dob, nationality)
        self.airline = airline
        self.title = title
        self.__tax_no = tax_no

    def get_airline(self):
        return self.airline

    def set_airline(self, new_airline):
        self.airline = new_airline
        name = self.get_full_name()
        print(f"Airline changed for person:  {name}\n New airline:   {self.airline}")

    def get_title(self):
        return self.title

    def set_title(self, new_title):
        self.title = new_title
        name = self.get_full_name()
        print(f"Job title changed for person:   {name}\n New title:   {self.title}")

    def get_tax_no(self):
        return self.__tax_no

    def set_tax_no(self, new_no):
        self.__tax_no = new_no
        name = self.get_full_name()
        print(f"Tax number updated for person:   {name}\n New tax no:   {self.__tax_no}")




# def __init__(self, full_name, airline, title, dob, tax_no, nationality):
crew1 = Staff('Steve', 'BA', 'Cabin Crew', '17/06/89', 7305734, 'USA')
crew2 = Staff('Caragh', 'BA', 'Cabin Crew', '29/05/95', 4846473, 'Kenya')
pilot = Staff('Martin', 'BA', 'Pilot', '19/11/68', 9927729, 'Switzerland')
copilot = Staff('Wessel', 'BA', 'Copilot', '20/03/92', 6229163, 'Netherlands')

