from subclass_attendee_report import *
from class_flights import *
from subclass_flight_report import *
from subclass_staff import *
from subclass_passengers import *

# Set up
pioneer = AttendeeReport('Pioneer')


# Explain
print("Test 1:")         # Append items to report list
print("Testing: append_manifest()...")
# Test
pioneer.append_manifest(passenger1)
pioneer.append_manifest(passenger2)

if passenger1 in pioneer.manifest:
    print("Append complete: ", True)
else:
    print("Append complete: ", False)
# Explain
print("\nTest 2:")         # Produce full report
print("Testing: print_manifest()...")
# Test
pioneer.print_manifest()
