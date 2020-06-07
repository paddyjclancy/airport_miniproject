from subclass_passengers import *


test_subject = Passenger('Patrick Clancy', '06/05/97', 'UK', '73469573')

# ----------------------------------------------------------
exp_econ_price = 300
# Test 1: Show passenger details
print("Testing method passenger_details()")
test_subject.passenger_details()
# ----------------------------------------------------------
# Test 2: Purchasing Ticket
print("\nTesting process of ticket purchase: Economy (BA-2)")
test_subject.purchase_ticket("Economy")
print(f"Values updated for passenger {test_subject.get_full_name()}:")
print(f"Boarding Pass:  {test_subject.boarding_pass} ")
print(f"Ticket Type: {test_subject.ticket_type}")
print(f"Ticket Price: {test_subject.ticket_price}")
# ----------------------------------------------------------
# Test 3: Boarding Pass
print("\nTesting set_boarding_pass():")
test_subject.set_boarding_pass()
print(f"Economy boarding pass:  {test_subject.boarding_pass} ")
test_subject.set_boarding_pass()
print(f"Economy boarding pass:  {test_subject.boarding_pass} ")
test_subject.set_boarding_pass()
print(f"Economy boarding pass:  {test_subject.boarding_pass} ")

test_subject.purchase_ticket("First")
test_subject.set_boarding_pass()
print(f"First boarding pass:  {test_subject.boarding_pass} ")
test_subject.set_boarding_pass()
print(f"First boarding pass:  {test_subject.boarding_pass} ")
test_subject.set_boarding_pass()
print(f"First boarding pass:  {test_subject.boarding_pass} ")

test_subject.purchase_ticket("Infant")
test_subject.set_boarding_pass()
print(f"Infant boarding pass:  {test_subject.boarding_pass} ")
test_subject.set_boarding_pass()
print(f"Infant boarding pass:  {test_subject.boarding_pass} ")
test_subject.set_boarding_pass()
print(f"Infant boarding pass:  {test_subject.boarding_pass} ")
# ----------------------------------------------------------
test_subject.purchase_ticket("Economy")
exp_boarding_pass = test_subject.boarding_pass
exp_passport_no = "73469573"
exp_ticket_type = "Economy"
# Test 4: Get Methods
print("\nTesting method:  get_ticket_type()")
output1 = test_subject.get_ticket_type()
print(f"Test result: {output1}")
print(output1 == exp_ticket_type)

print("\nTesting method: get_passport_number()")
output2 = test_subject.get_passport_number()
print(f"Test result: {output2}")
print(output2 == exp_passport_no)

print("\nTesting method: get_boarding_pass() ")
output3 = test_subject.get_boarding_pass()
print(f"Test result: {output3}")
print(output3 == exp_boarding_pass)
# ----------------------------------------------------------
exp_new_pp = "9292888"
exp_new_ticket = "First"
# Test 5: Remaining Set Methods
print("\nTesting method: set_passport_number() ")
test_subject.set_passport_number("9292888")
output4 = test_subject.get_passport_number()
print(f"Test result:  {output4}")
print(output4 == exp_new_pp)

print("\nTesting method: set_ticket_type()  ")
test_subject.set_ticket_type("First")
output5 = test_subject.get_ticket_type()
print(f"Test result:  {output5}")
print(output5 == exp_new_ticket)