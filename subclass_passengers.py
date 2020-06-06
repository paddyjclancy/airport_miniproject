from class_people import *

class Passenger(People):

    def __init__(self, full_name, dob, nationality, passport_no, ticket, boarding_pass):
        super().__init__(full_name, dob, nationality)
        self.BoardingPass = boarding_pass
        self.Passport = passport_no
        self.Ticket = ticket.capitalize()
#       ticket to move to other class?


passenger1 = Passenger('Paddy', '06/05/97', 'British', '7349573', 'economy', 'BA-5285-9475')
passenger2 = Passenger('Georgina', '31/07/98', 'British', '3492642', 'first', 'BA-8237-8273')
passenger3 = Passenger('Lauren', '08/04/16', 'Austria', '63853975', 'infant', 'BA-2298-0105')
