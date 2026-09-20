import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
special_chars = ['!', '#', '$', '%', '&', '(', ')', '*', '+']   

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))
nr_symbols = int(input("How many special characters would you like in your password?\n"))

# char = random.choices(alphabet, k=nr_letters)
# num = random.choices(numbers, k=nr_numbers)
# sym = random.choices(special_chars, k=nr_symbols)
# # print(char, num, sym)

# password_list = char + num + sym


# password = ""
# for i in password_list:
#     password += str(i)
# print("Your password is: " + password)

# shuffled_password = ""
# random.shuffle(password_list)
# for i in password_list:
#     shuffled_password += str(i)
# print("Your password is: " + shuffled_password)


password = ""
for i in range(0, nr_letters):
    char = random.choice(alphabet)
    password += char
for i in range(0, nr_numbers):
    num = random.choice(numbers)
    password += str(num)
for i in range(0, nr_symbols):
    sym = random.choice(special_chars)
    password += str(sym)
print(f"Your password is: {password}")

          