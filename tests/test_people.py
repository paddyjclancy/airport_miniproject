from class_people import *


test_subject = People("Steve Martin", "11/09/65", "USA")

# ----------------------------------------------------------
exp_name = "Steve Martin"
exp_dob = "11/09/65"
exp_nat = "USA"
# Test 1: Get Methods
print("Testing get methods with instance: test_subject = People('Steve Martin', '11/09/65', 'USA')")
print("\nTesting method:  get_full_name()")
output1 = test_subject.get_full_name()
print(f"Test result: {output1}")
print(output1 == exp_name)

print("\nTesting method:  get_dob()")
output2 = test_subject.get_dob()
print(f"Test result: {output2}")
print(output2 == exp_dob)

print("\nTesting method:  get_nationality()")
output3 = test_subject.get_nationality()
print(f"Test result: {output3}")
print(output3 == exp_nat)

# ----------------------------------------------------------
new_name = "Steve Austin"
new_dob = "11/09/66"
new_nat = "Canada"
# Test 2: Set Methods
print("Testing set methods with instance: test_subject = People('Steve Martin', '11/09/65', 'USA')")
print("\nTesting method:  set_full_name()")
test_subject.set_full_name("Steve Austin")
print(f"Test result: {exp_name} --> {test_subject.get_full_name()}")
print(test_subject.get_full_name() == new_name)

print("\nTesting method: set_dob()")
test_subject.set_dob("11/09/66")
print(f"Test result: {exp_dob} --> {test_subject.get_dob()}")
print(test_subject.get_dob() == new_dob)

print("\nTesting method: set_nationality()")
test_subject.set_nationality("Canada")
print(f"Test result: {exp_nat} --> {test_subject.get_nationality()}")
print(test_subject.get_nationality() == new_nat)