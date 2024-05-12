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
number = random.randrange(100)  
print("Number:", number)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

def game(attemps):
    while attemps != 0:
        print(f"You have {attemps} attemps remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == number:
            return "You guessed it right!."
        elif guess < number:
            print("Too low")
            attemps-= 1
        elif guess > number:
            print("Too high")
            attemps -= 1
    return "You've run out of guesses, you lose."

if difficulty == "hard":
    print(game(5))
elif difficulty == "easy":
    print(game(10))
else:
    print("Invalid input.")
