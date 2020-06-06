from class_people import *

class Staff(People):

    def __init__(self, full_name, dob, nationality, title):
        super().__init__(full_name, dob, nationality)
        self.Title = title



crew1 = Staff('Steve', '17/06/89', 'French', 'Cabin Crew')
crew2 = Staff('Caragh', '29/05/95', 'Kenya', 'Cabin Crew')
pilot = Staff('Martin', '19/11/68', 'Switzerland', 'Pilot')
copilot = Staff('Wessel', '20/03/92', 'Netherlands', 'Copilot')