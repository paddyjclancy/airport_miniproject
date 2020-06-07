from subclass_flight_report import *
from subclass_staff import *


# Set up
pioneer = FlightReport('Pioneer', '0800', 'Paris', 290, 'A321', 300)


# Explain
print("---------------------------------------------------------------------------")
print("Test 1: Making adjustment to flight report (delays, change of plane, etc...")
print("Testing: delay()")
print("Delaying departure time by one hour...")
# Test
pioneer.delay("0945")
print("Result: ", pioneer.departure == "0945")
# Explain
print("\nTesting: divert()")
print("Changing destination from Paris to Toulouse...")
# Test
pioneer.divert("Toulouse")
print("Result: ", pioneer.destination == "Toulouse")
# Explain
print("\nTesting: alter_aircraft()")
print("Changing aircraft from A321 to A320...")
# Test
pioneer.alter_aircraft("A320")
print("Result: ", pioneer.plane == "A320")

# Explain
print("\n---------------------------------------------------------------------------")
print("Test 2: Produce full report - aesthetically")
print("Testing: show_report()")
print("Printing flight report: Pioneer...")
# Test
print("\n")
pioneer.show_report()


# Further steps:
#       Automate ETA calc. by adding method and required attributes (avg speed)
#       Add user friendly module
