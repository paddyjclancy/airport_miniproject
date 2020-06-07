from subclass_passengers import *
from class_flights import *


pioneer = Flight('Pioneer', '0800', 'Paris', 290, 'A321', 300)

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

print('Current flight in progress: ')
print(Flight.instances)

while objective != "Exit":
    objective = input(
        "\nWhat service would you like to access? \n Flight Status \n Flight Report \n Assign Staff \n Add Passenger \n Exit     \n                                 ")

    if objective == "Add Passenger":
        flight = input("Enter desired flight:   ")
        new_name = input("Enter passenger name:   ")
        new_dob = input("Enter passenger dob:   ")
        new_nationality = input("Enter passenger nationality:   ")
        new_pp = input("Enter passenger passport details:   ")
        new_t_type = input("Requested ticket type:   ")
        new_bp_raw = "BA-", str(randint(999, 9999)), "-", str(randint(999, 9999))
        new_bp = ''.join(new_bp_raw)

        passenger4 = Passenger(new_name, new_dob, new_nationality, new_pp, new_t_type, new_bp)
        passenger4.passenger_details()
        # Needs appending
    elif objective == "Flight Status":
        break
    elif objective == "Flight Report":
        break
    elif objective == "Assign Staff":
        break
    else:
        break

# new passenger
# flight status
# flight report
# assign staff
