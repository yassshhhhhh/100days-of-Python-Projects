import random
logo = """                                                             
 _____                    _   _                        _             
|   __|_ _ ___ ___ ___   | |_| |_ ___    ___ _ _ _____| |_ ___ ___   
|  |  | | | -_|_ -|_ -|  |  _|   | -_|  |   | | |     | . | -_|  _|  
|_____|___|___|___|___|  |_| |_|_|___|  |_|_|___|_|_|_|___|___|_|                                                                                                                                                                                                                                                                             
"""
print(logo)
print("Welcome to Guess the number!")
print("I'm thinking of a number between 1 and 100.")
number = random.randrange(1, 100)  
print("Number:", number)
EASY_LEVEL = 10
HARD_LEVEL = 5
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

def game(attemps):
    while attemps != 0:
        print(f"You have {attemps} attemps remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == number:
            return f"You guessed it right!, the number was {number}."
        elif guess < number:
            print("Too low \nGuess again")

            attemps-= 1
        elif guess > number:
            print("Too high \nGuess again")
            attemps -= 1
    return "Ohh noo! You've run out of guesses, you lose."

if difficulty == "hard":
    print(game(HARD_LEVEL))
elif difficulty == "easy":
    print(game(EASY_LEVEL))
else:
    print("Invalid input.")
