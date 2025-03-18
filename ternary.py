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

#Iterable
for x in "Python":
    print(x)

number = 100
while number > 0:
    print(number)
    number //= 2    # floor division
else:
    print("Done")
"""
    command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)
else:
    print("Done")

#Infinite loop
while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break
"""
#Even numbers
count = 0
for number in range(1,10):
    if number % 2 == 0:
        print(number)
        count += 1
print(f"We have {count} even numbers")