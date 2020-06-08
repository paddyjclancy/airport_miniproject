import time
from subclass_passengers import *
from subclass_staff import *
from class_flights import *


this_flight = pioneer

staff_roster = [pilot1, pilot2, pilot3, copilot1, copilot2, copilot3, copilot4, crew1, crew2, crew3, crew4, crew5, crew6]
this_flight.append_manifest(pilot1)
this_flight.append_manifest(copilot1)
this_flight.append_manifest(passenger1)
this_flight.append_manifest(passenger2)

password = "happy flighting"
entry = ""
objective = "".capitalize().strip()

while entry != password:

    entry = (input("Please enter password:     "))

    if entry.lower() == password:
        print("Welcome...")
        break
    else:
        print("Incorrect password")

time.sleep(1)
print("\nCurrent flights in progress: ")
for i in Flight.instances:
    print(i)

time.sleep(1)
print(f"\nFlight accessed: {this_flight.flight}")

while objective.strip().lower() != "exit":
    time.sleep(1)
    objective = input(
        "\nWhat service would you like to access? \n Flight Status \n Flight Manifest \n Assign Staff \n Add "
        "Passenger \n Exit     \n                         ")

    if objective.strip().lower() == "add passenger":
        more_passengers = 'hmm'

        while more_passengers.strip().upper():
            pass_id = 1
            more_passengers = input(f"\nAdd passenger to flight - {this_flight.flight}?  (Y/N)   ")
            if more_passengers.strip().upper() == "N":
                break
            new_name = input("Enter passenger name:   ")
            new_dob = input("Enter passenger dob:   ")
            new_nationality = input("Enter passenger nationality:   ")
            new_pp = input("Enter passenger passport details:   ")
            new_t_type = input("Requested ticket type:   ")
            new_passenger = Passenger(new_name, new_dob, new_nationality, new_pp, pass_id, new_t_type)
            new_passenger.set_boarding_pass()
            this_flight.append_manifest(new_passenger)
            pass_id += 1

        print(f"\nPassengers confirmed on flight - {this_flight.flight}:")
        for p in this_flight.manifest:
            if isinstance(p, Passenger):
                print(p.get_full_name(), "-     Passport: ", p.get_passport_number())

    elif objective.strip().lower() == "flight status":
        edit = ""
        print(f"\n")
        this_flight.show_report()

        while edit.strip().upper() != "EXIT":
            edit = input(f"\nMake changes to flight: {this_flight.flight}? \n   DELAY / DIVERT / CHANGE / EXIT      ")
            if edit.strip().upper() == "DELAY":
                new_time = input("New departure:  ")
                this_flight.delay(new_time)
            elif edit.strip().upper() == "DIVERT":
                new_destination = input("New destination:   ")
                this_flight.divert(new_destination)
            elif edit.strip().upper() == "CHANGE":
                new_plane = input("New plane:   ")
                this_flight.alter_aircraft(new_plane)

        time.sleep(1)
        print(f"\n Updated flight status:")
        this_flight.show_report()

    elif objective.strip().lower() == "flight manifest":
        which_manifest = ""

        while which_manifest.strip().upper() != "EXIT":
            which_manifest = input("\nWhich manifest? \n   PASSENGER / CREW / FULL / EXIT    ")
            if which_manifest.strip().upper() == "FULL":
                this_flight.show_manifest()
            if which_manifest.strip().upper() == "CREW":
                for p in this_flight.manifest:
                    if isinstance(p, Staff):
                        print(vars(p))
            if which_manifest.strip().upper() == "PASSENGER":
                for q in this_flight.manifest:
                    if isinstance(q, Passenger):
                        print(vars(q))

    elif objective.strip().lower() == "assign staff":
        assigned = ""
        print(f"Current staff assigned to flight: {this_flight.flight}")
        for p in this_flight.manifest:
            if isinstance(p, Staff):
                print(p.get_full_name())
        while assigned.strip().lower() != "x":
            assigned = input("\nEnter staff to assign. Enter 'x' when complete:   ")
            for s in staff_roster:
                staff_name = s.get_full_name()
                if assigned == staff_name:
                    this_flight.append_manifest(s)
        print("\nStaff assigned to flight:")
        for p in this_flight.manifest:
            if isinstance(p, Staff):
                print(p.get_full_name())


print("Logging off...")
