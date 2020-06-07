from class_flights import *
from class_people import *
from subclass_passengers import *
from subclass_staff import *

class AttendeeReport(Flight):

    def __init__(self, flight, departure, manifest=None):
        super().__init__(flight, departure)
        self.manifest = manifest
        if manifest is None:
            self.manifest = []

    def append_manifest(self, passenger):
        self.manifest.append(passenger)

    def full_manifest(self):
        print(f"\nManifest for personnel on flight {self.flight}: ")
        for person in self.manifest:
            print(vars(person))


# Append list with dict

# Passenger: name, dob, passport_no, ticket_type(sales), boarding_pass(sales)
# Crew: name, dob, title

# Name, title, dob, passport_no, ticket_type, boarding_pass     <-----------
# title - attendant, pilot, passenger (if crew is not True) <-----------

# Present aesthetically
# Display everything
# for key, value in dict.items():
#    print(key, ": ", value)