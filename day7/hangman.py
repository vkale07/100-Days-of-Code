import random
import hangman_words  
from hangman_art import stages, logo

lives = 6
print(logo)

# word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

placeholder = ""
placeholder += "_" * len(chosen_word)
print(placeholder)

game_over = False
correct_letter = []

while not game_over:

    print(f"******************* {lives}/6 lives left *******************")
    user_guess = input("Guess a letter: ").lower()

    if user_guess in correct_letter:
        print(f"You already guessed that letter : {user_guess}")
        

    display = ""

    for letter in chosen_word:
        if letter == user_guess:
            display += letter
            correct_letter.append(letter)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"
    print(display)

    if user_guess not in chosen_word:
        lives -= 1
        print(f"You guessed {user_guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(f"******************* IT was: {chosen_word}, YOU LOSE! *******************")


    if "_" not in display:
        game_over = True
        print("******************* YOU WIN! *******************")

    print(stages[lives])