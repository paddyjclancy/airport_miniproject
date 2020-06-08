from class_people import *


class Staff(People):

    def __init__(self, full_name, airline, title, dob, tax_no, nationality):
        super().__init__(full_name, dob, nationality)
        self.airline = airline
        self.title = title
        self.__tax_no = tax_no
        self.details = {}

    def get_airline(self):
        return self.airline

    def set_airline(self, new_airline):
        self.airline = new_airline
        name = self.get_full_name()
        print(f"Airline changed for person:  {name}\nNew airline:   {self.airline}")

    def get_title(self):
        return self.title

    def set_title(self, new_title):
        self.title = new_title
        name = self.get_full_name()
        print(f"Job title changed for person:   {name}\nNew title:   {self.title}")

    def get_tax_no(self):
        return self.__tax_no

    def set_tax_no(self, new_no):
        self.__tax_no = new_no
        name = self.get_full_name()
        print(f"Tax number updated for person:   {name}\nNew tax no:   {self.__tax_no}")


    def staff_details(self):
        self.details = {
            "Name": self.get_full_name(),
            "DOB": self.get_dob(),
            "Nationality": self.nationality,
            "Title": self.title,
            "Airline": self.airline,
            "Tax No.": self.__tax_no,
        }
        for key, value in self.details.items():
            print(key, ": ", value)

# STAFF ROSTER
crew1 = Staff('Steve Martin', 'BA', 'Cabin Crew', '17/06/89', 7305734, 'USA')
crew2 = Staff('Caragh Cowan', 'BA', 'Cabin Crew', '29/05/95', 4846473, 'Kenya')
crew3 = Staff('Chloe McDonald', 'BA', 'Cabin Crew', '29/11/97', 9384322, 'UK')
crew4 = Staff('Laura Philips', 'BA', 'Cabin Crew', '04/08/96', 7731032, 'UK')
crew5 = Staff('Fergus McFadden', 'Aer Lingus', 'Cabin Crew', '14/01/95', 4479756, 'UK')
crew6 = Staff('Niamh Quillagan', 'Aer Lingus', 'Cabin Crew', '13/04/93', 1004624, 'Ireland')

pilot1 = Staff('Martin Clunes', 'BA', 'Pilot', '19/11/68', 9927729, 'Switzerland')
pilot2 = Staff('Ed Balls', 'BA', 'Pilot', '18/10/71', 4137972, 'UK')
pilot3 = Staff('Declan Smith', 'Aer Lingus', 'Pilot', '06/06/78', 8493799, 'Ireland')
copilot1 = Staff('Wessel Withoos', 'BA', 'Copilot', '20/03/92', 6229163, 'Netherlands')
copilot2 = Staff('Fabio Capello', 'BA', 'Copilot', '23/04/82', 5528631, 'Italy')
copilot3 = Staff('Wanda McVey', 'American Airlines', 'Copilot', '07/02/88', 7583957, 'USA')
copilot4 = Staff('James Jamison', 'BA', 'Copilot', '04/01/86', 6202775, 'UK')
