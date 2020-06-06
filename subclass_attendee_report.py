from class_flights import *
from class_people import *
from subclass_passengers import *
from subclass_staff import *


# Append list with dict

# Passenger: name, dob, passport_no, ticket_type(sales), boarding_pass(sales)
# Crew: name, dob, title

# Name, title, dob, passport_no, ticket_type, boarding_pass     <-----------
# title - attendant, pilot, passenger (if crew is not True) <-----------

# Present aesthetically
# Display everything
# for key, value in dict.items():
#    print(key, ": ", value)


class AttendeeReport(Flight):

    def __init__(self, flight, manifest=None):
        self.flight = flight.capitalize()
        self.manifest = manifest
        if manifest is None:
            self.manifest = []


    def append_manifest(self, passenger):
        self.manifest.append(passenger)


    def print_manifest(self):
        for person in self.manifest:
            print(vars(person))