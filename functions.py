def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")


greet("Kiran", "Verma")

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total
print(multiply(2, 3, 4, 5))