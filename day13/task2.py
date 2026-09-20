# age = int(input("What is your age? ")) # on execution when we pass string to this it will throw ValueError

# if age > 18:
#     print("You can drive at age {age}.")

try:
    age = int(input("What is your age? "))
except ValueError:
    print("You have typed an invalid input, please try again and enter a number like 20.")
    age = int(input("What is your age? "))

if age > 18:
    print(f"You can drive at age {age}.")