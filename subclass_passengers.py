from class_people import *

class Passenger(People):

    def __init__(self, full_name, dob, nationality, passport_no, ticket_type, boarding_pass):
        super().__init__(full_name, dob, nationality)
        self.boarding_pass = boarding_pass
        self.passport_no = passport_no
        self.ticket_type = ticket_type.capitalize()
        self.ticket_price = int
        if self.ticket_type == "First":
            self.ticket_price = 1000
        elif self.ticket_type == "Infant":
            self.ticket_price = 0
        elif self.ticket_type == "Economy":
            self.ticket_price = 300

    def get_boarding_pass(self):
        return self.boarding_pass

    def set_boarding_pass(self, new_bp):
        self.boarding_pass = new_bp
        name = self.get_full_name()
        print(f"Boarding pass updated for passenger:   {name}\n New boarding pass:   {self.boarding_pass}")

    def get_passport_number(self):
        return self.passport_no

    def set_passport_number(self, new_pp):
        self.passport_no = new_pp
        name = self.get_full_name()
        print(f"Passport number updated for passenger:   {name}\n New number:   {self.passport_no}")

    def get_ticket_type(self):
        print(f"{self.ticket_type} ticket, price: {self.ticket_price}")

    def set_ticket_type(self, new_ticket):
        self.ticket_type = new_ticket
        name = self.get_full_name()
        print(f"Ticket type updated for passenger: {name}, to {self.ticket_type}")


passenger1 = Passenger('Paddy', '06/05/97', 'British', '7349573', 'economy', 'BA-5285-9475')
passenger2 = Passenger('Georgina', '31/07/98', 'British', '3492642', 'first', 'BA-8237-8273')
passenger3 = Passenger('Lauren', '08/04/16', 'Austria', '63853975', 'infant', 'BA-2298-0105')
