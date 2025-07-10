import random

print("Welcome to the Number Guessing Game!")

secret_number = random.randint(1, 100)
print("Secret number is:", secret_number)  # You can remove this in final version

max_guesses = int(input("How many guesses do you want? "))
guess_count = 0

while guess_count < max_guesses:
    guess = int(input("Enter your guess: "))
    guess_count += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Correct! You guessed it in {guess_count} attempts.")
        break

if guess != secret_number:
    print(f"You lost! The correct number was {secret_number}.")
