import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Print a specific choice
# print(paper)   
item = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)

if user_choice >= 0 and user_choice <= 2:
    print(item[user_choice])

print("Computer chose:")
print(item[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
elif item[user_choice] == item[computer_choice] :
    print("It's a draw!")
elif item[user_choice] == rock and item[computer_choice] == scissors:
    print("you win")
elif item[user_choice] == scissors and item[computer_choice] == paper:
    print("you win")
elif item[user_choice] == paper and item[computer_choice] == rock:
    print("you win")
else:
    print("you lose")
