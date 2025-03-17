#ForLoop
successfull = True
for number in range(3):
    print("number",number + 1, (number + 1) * ".") 
    if successfull:
        print("Email sent")
        break
else:
    print("Email not sent")
# Nested loop
for x in range(4):
    for y in range(3):
        print(f"({x},{y})") 
