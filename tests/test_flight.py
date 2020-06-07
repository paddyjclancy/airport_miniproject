from class_flights import *
from subclass_passengers import *
from subclass_staff import *


pioneer = Flight('Pioneer', '0800', 'Paris', '1h20m', 'A321', 300)

# ----------------------------------------------------------
# Test 1: Making adjustment to flight report
print("Testing method: delay()")
print("Delaying departure time by one hour...")
pioneer.delay("0945")
print("Result: ", pioneer.departure == "09:45")

print("\nTesting method: divert()")
print("Changing destination from Paris to Toulouse...")
pioneer.divert("Toulouse")
print("Result: ", pioneer.destination == "Toulouse")

print("\nTesting method: alter_aircraft()")
print("Changing aircraft from A321 to A320...")
pioneer.alter_aircraft("A320")
print("Result: ", pioneer.plane == "A320")


# ---------------------------------------------------------
# Test 2: Produce full report - aesthetically
print("\nTesting: show_report()...")

pioneer.show_report()

# ----------------------------------------------------------
# Test 1: Append items to report list
print("\nTesting: append_manifest()...")
print(f"Current manifest: {pioneer.manifest}")
pioneer.append_manifest(crew1)
pioneer.append_manifest(crew2)
pioneer.append_manifest(pilot)
pioneer.append_manifest(copilot)
pioneer.append_manifest(passenger1)
pioneer.append_manifest(passenger2)
pioneer.append_manifest(passenger3)

if passenger1 and passenger2 and passenger3 in pioneer.manifest:
    print("Append complete: ", True)
else:
    print("Append complete: ", False)

# ----------------------------------------------------------
# Test 2: Show manifest
print("\nTesting method:  full_manifest()...")
pioneer.show_manifest()


# Further steps:
#       Sort manifest through hierarchy - pilot, copilot, crew, first, economy, infant
#       Create separate manifests - staff, passengers, first, infants
#       Improve visual aesthetic of manifest
