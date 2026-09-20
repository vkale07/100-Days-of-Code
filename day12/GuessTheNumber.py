import random
from art import number_guess_logo
print(number_guess_logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

num_to_guess = random.randint(1, 100)
print(f"You need to guess this number : {num_to_guess}")

choice = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
attempt = 0
if choice == "easy":
    attempt = 10
    print(f"You have {attempt} attempts remaining to guess the number.")
else:
    attempt = 5
    print(f"You have {attempt}  attempts remaining to guess the number.")

# print(attempt)

while attempt > 0 :
    user_guess = int(input("Make a guess : "))
    if num_to_guess > user_guess:
        print("Too low.\nPlease guess again")
    elif num_to_guess < user_guess:
        print("Too high.\nPlease guess again")
    elif num_to_guess == user_guess:
        print(f"You got it!, that's the number {user_guess}")
        break

    attempt -= 1
    print(f"You have {attempt} attempts remaining to guess the number.")