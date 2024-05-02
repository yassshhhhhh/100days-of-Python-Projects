import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 of Rock, 1 for Paper, 2 for Scissors:\n"))


if user_choice < 0 or user_choice >= 3 :
  print("You entered an invalid input, You Lose.")

else: 
  print("You chose:")
  print(game_images[user_choice])
  computer_choice = random.randint(0, 2)
  print("Computer chose:")
  print(game_images[computer_choice])
  if user_choice == computer_choice:
    print("It's a draw")
  elif user_choice == 0 and computer_choice == 2:
    print("You win!")  
  elif user_choice == 2 and computer_choice == 0:
    print("You lose!")
  elif user_choice > computer_choice:
    print("You win!")
  elif user_choice < computer_choice:
    print("You lose")




# import random

# Your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors."))

# computer_choice = random.randint(0,2)

# if Your_choice == 0 and computer_choice == 0:
#   print(rock)
#   print("Computer chose: ")
#   print(rock)
#   print("It's a draw.")
# elif Your_choice == 0 and computer_choice == 1:
#   print(rock)
#   print("Computer chose: ")
#   print(paper)
#   print("You lose.")
# elif Your_choice == 0 and computer_choice == 2:
#   print(rock)
#   print("Computer chose: ")
#   print(scissors)
#   print("You win.")
# elif Your_choice == 1 and computer_choice == 0:
#   print(paper)
#   print("Computer chose: ")
#   print(rock)
#   print("You win.")
# elif Your_choice == 1 and computer_choice == 1:
#   print(paper)
#   print("Computer chose: ")
#   print(paper)
#   print("It's a draw.")
# elif Your_choice == 1 and computer_choice == 2:
#   print(paper)
#   print("Computer chose: ")
#   print(scissors)
#   print("You lose.")
# elif Your_choice == 2 and computer_choice == 0:
#   print(scissors)
#   print("Computer chose: ")
#   print(rock)
#   print("You lose.")
# elif Your_choice == 2 and computer_choice == 1:
#   print(scissors)
#   print("Computer chose: ")
#   print(paper)
#   print("You win.")
# elif Your_choice == 2 and computer_choice == 2:
#   print(scissors)
#   print("Computer chose: ")
#   print(scissors)
#   print("It's a draw.")
# else:
#   print("You typed an invalid number, you lose!")