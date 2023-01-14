import random
import os

def guess_number():
    print("Welcome to the Number guessing Game!")
    print("I am thinking of a number between 1 and 100")
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if level == "easy":
        guess_count = 10
    elif level == "hard":
        guess_count = 5
        
    print(f"You have {guess_count} attempts remaining to guess the number.")


    actual_number = random.randint(1,101)
    print(actual_number)
    continue_game = True

    while continue_game:
        Guess = int(input("Make a guess: "))
        guess_count -= 1
        if Guess == actual_number:
            print("You guessed it correctly..!!")
            continue_game = False
        else:
            if Guess > actual_number:
                print("Too high.\nGuess again.")
            elif Guess < actual_number:
                print("Too low.\nGuess again")
            print(f"You have {guess_count} attempts remaining to guess the number.")
        if guess_count == 0:
            continue_game = False

    play_again= input("Type 'y' if you want to try again: ")
    if play_again == 'y':
        os.system('cls')
        guess_number()   
guess_number()