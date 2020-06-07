from random import randint

from class_people import *


class Passenger(People):

    def __init__(self, full_name, dob, nationality, passport_no, ticket_type=None, ticket_price=None,
                 boarding_pass=None):
        super().__init__(full_name, dob, nationality)
        self.boarding_pass = boarding_pass
        self.passport_no = passport_no
        self.ticket_type = ticket_type
        self.ticket_price = ticket_price

    def purchase_ticket(self, ticket_type):
        if ticket_type == "First":
            self.ticket_type = "First"
            self.ticket_price = 1000
            self.set_boarding_pass()

        elif ticket_type == "Infant":
            self.ticket_type = "Infant"
            self.ticket_price = 0
            self.set_boarding_pass()

        elif ticket_type == "Economy":
            self.ticket_type = "Economy"
            self.ticket_price = 300
            self.set_boarding_pass()

    def get_boarding_pass(self):
        return self.boarding_pass

    def set_boarding_pass(self):
        if self.ticket_type == "First":
            new_bp = "BA-1", str(randint(99, 999)), "-", str(randint(999, 9999))
            self.boarding_pass = ''.join(new_bp)
        elif self.ticket_type == "Infant":
            new_bp = "BA-9", str(randint(99, 999)), "-", str(randint(999, 9999))
            self.boarding_pass = ''.join(new_bp)
        elif self.ticket_type == "Economy":
            new_bp = "BA-2", str(randint(99, 999)), "-", str(randint(999, 9999))
            self.boarding_pass = ''.join(new_bp)

    def get_passport_number(self):
        return self.passport_no

    def set_passport_number(self, new_pp):
        self.passport_no = new_pp
        name = self.get_full_name()
        return f"Passport number updated for passenger:   {name}\n New number:   {self.passport_no}"

    def get_ticket_type(self):
        return self.ticket_type

    def set_ticket_type(self, new_ticket):
        self.ticket_type = new_ticket
        name = self.get_full_name()
        return f"Ticket type updated for passenger: {name}, to {self.ticket_type}"

    def passenger_details(self):
        report = vars(self)
        for key, value in report.items():
            return key.capitalize(), ": ", value


passenger1 = Passenger('Paddy', '06/05/97', 'British', '73469573')
passenger2 = Passenger('Georgina', '31/07/98', 'British', '34392642')
passenger3 = Passenger('Lauren', '08/04/16', 'Austria', '63856975')
