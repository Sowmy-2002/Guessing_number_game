
#GUESSING GAME
#random is used to generate random number
import random

def guessing_game():
    # Generate a random number between 1 and 10
    secret_num = random.randint(1, 10)

    print("Welcome to the Guess the Number game!")
    print("I've selected a number between 1 and 10. You have 3 attempts to guess it.")

    attempts = 3

    for attempt in range(1, attempts + 1):
        # Get user input
        guess = int(input(" Enter your guess: "))

        # Check if the guess is correct
        if guess == secret_num:
            print(f"Congratulations! You guessed the number {secret_number} correctly.")
            break
        elif guess < secret_num:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

    else:
        print(f"Sorry, you've run out of attempts.")

if __name__ == "__main__":
    guessing_game()
