import random

# Set the range for the guessing game
min_number = 1
max_number = 100

# Generate a random number within the range
secret_number = random.randint(min_number, max_number)

# Initialize variables for the game loop
num_guesses = 0
guessed_correct = False

# Welcome message
print("Welcome to the Guessing Game!")

while not guessed_correct:
    # Get the user's guess
    try:
        guess = int(input(f"Guess a number between {min_number} and {max_number} (inclusive): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    num_guesses += 1

    # Check the guess
    if guess < secret_number:
        print("Too low! Guess again.")
    elif guess > secret_number:
        print("Too high! Guess again.")
    else:
        guessed_correct = True

# Congratulate the user on winning
print(f"Congratulations! You guessed the number in {num_guesses} tries.")
