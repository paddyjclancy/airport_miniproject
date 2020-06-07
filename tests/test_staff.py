from subclass_staff import *


test_subject = Staff("Steve Martin", "BA", "Copilot", "11/09/65", 34567, "USA")

# ----------------------------------------------------------
exp_airline = "BA"
exp_title = "Copilot"
exp_tax = 34567
# Test 1: Get Methods
print("Testing get methods with instance: test_subject = Staff('Steve Martin', 'BA', 'Copilot', '11/09/65', 34567, 'USA')")
print("\nTesting method get_airline()")
output1 = test_subject.get_airline()
print(f"Test result: {output1}")
print(output1 == exp_airline)

print("\nTesting method get_title()")
output2 = test_subject.get_title()
print(f"Test result: {output2}")
print(output2 == exp_title)

print("\nTesting method get_tax_no()")
output3 = test_subject.get_tax_no()
print(f"Test result: {output3}")
print(output3 == exp_tax)

# ----------------------------------------------------------
new_airline = "Canadian Airlines"
new_title = "Pilot"
new_tax = 76543
# Test 2: Set Methods
print("Testing set methods with instance: test_subject = Staff('Steve Martin', 'BA', 'Copilot', '11/09/65', 34567, 'USA')")
print("\nTesting method set_airline()")
test_subject.set_airline("Canadian Airlines")
print(f"Test result: {exp_airline} --> {test_subject.get_airline()}")
print(test_subject.get_airline() == new_airline)

print("\nTesting method set_title()")
test_subject.set_title("Pilot")
print(f"Test result: {exp_title} --> {test_subject.get_title()}")
print(test_subject.get_title() == new_title)

print("\nTesting method set_tax_no")
test_subject.set_tax_no(76543)
print(f"Test result: {exp_tax} --> {test_subject.get_tax_no()}")
print(test_subject.get_tax_no() == new_tax)
