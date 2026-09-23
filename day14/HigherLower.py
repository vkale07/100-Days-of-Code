import random
import art
from game_data import data

print(art.logo)
x = random.choice(data)

game_continue = True
score = 0

while game_continue:

    y = random.choice(data)
    if x == y:
        y = random.choice(data)
    
    print(f"Compare A: {x['name']}, {x['description']}, {x['country']}")
    first_value = x["follower_count"]

    print(art.vs)

    # y = random.choice(data)
    print(f"Against B: {y['name']}, {y['description']}, {y['country']}")
    sec_value = y["follower_count"]

    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    print(art.logo)

    if user_guess == 'a':
        if first_value > sec_value:
            score += 1
            print(f"You're right! Current Score: {score}")      
        else:
            print(f"Sorry, that's wrong! Final score: {score}")
            game_continue = False
    elif user_guess == 'b':
        if sec_value > first_value:
            score += 1
            print(f"You're right! Current Score: {score}")
        else:
            print(f"Sorry, that's wrong! Final score: {score}")
            game_continue = False
    else:
        game_continue = False

    x = y

