from class_airport import *

# Parent Class = People()
    # full_name, dob, nationality
# Sub classes = Staff, Passengers, Sales
    # Staff() - title
    # Passengers() - passport_no
    # Sales() - ticket_type, boarding_pass

class People(Airport):

    def __init__(self, full_name, dob, nationality):
        self.Name = full_name
        self.DOB = dob
        self.Nationality = nationality
