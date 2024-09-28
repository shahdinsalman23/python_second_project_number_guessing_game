import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

while True:
    # Ask the user to guess the number
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        # Check if the guess is correct
        if guess == secret_number:
            print(" Congratulations! You guessed it!")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
    else:
        print("Invalid input. Please enter a number.")