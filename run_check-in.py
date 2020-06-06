from class_people import *
from subclass_passengers import *
from subclass_staff import *
from class_flights import *
from subclass_flight_report import *

pioneer = FlightReport('Pioneer', '0800', 'Paris', 290, 'A321', 300)

password = 'Happy flighting'
entry = ''
objective = ''.capitalize().strip()

while entry != password:

    entry = (input("Please enter password:     ")).capitalize()

    if entry == password:
        print("Welcome...")
        break
    else:
        print("Incorrect password")


print('Current flights in progress: ')
print(Flight.instances)


while objective != "Exit":
    objective = input("\nWhat service would you like to access? \n Flight Status \n Flight Report \n Assign Staff \n Add Passenger \n Exit     \n                                 ")

    if objective == "New Passenger":
        break
    elif objective == "Flight Status":
        break
    elif objective == "Flight Report":
        break
    elif objective == "Assign Staff":
        break
    else:
        break

#new passenger
#flight status
#flight report
#assign staff
