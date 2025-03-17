age =32
message = "You are old enough to vote!" if age >= 18 else "You are not old enough to vote!"
print(message)

# Logical operators
high_income = True
good_credit = True
student = False
message = "Eligible for loan" if not student and (good_credit or high_income) else "Not eligible for loan"
print(message)

#chaining comparison operators
age = 22
message = "Eligible" if 18 <= age < 65 else "Not eligible"
print(message)
