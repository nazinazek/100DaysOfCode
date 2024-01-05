import art
import random


def number_guess(number, guess):
    if number < guess:
        return print("Too high.\nGuess again.")
    elif number > guess:
        return print("Too low.\nGuess again.")
    else:
        return print(f"You got it! The answer was {guess}")
    

print(art.logo)
print("Welcome to the Number Guessing Game!")
guessed_number = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100")
print(f"Pssst, the correct answer is {guessed_number}")
game_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if game_level == 'easy':
    attempt = 10
else:
    attempt = 5

while attempt >= 0:
    if attempt != 0:
        print(f"You have {attempt} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        number_guess(guessed_number, user_guess)
    else :
        print("You've run out of guesses, you lose.")
    attempt -= 1