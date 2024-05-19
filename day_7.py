import random
import day_7_words 
from day_7_arts import logo, stages

word_list = day_7_words.words_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

position = 0
while "_" in display:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You have already entered {guess}.")

    for letter in chosen_word:
        position += 1
        if letter == guess:
            display[position - 1] = letter

    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is not in the word, You are left with {lives} lives.")
        if lives == 0:
            print("You lose!")
            break
            
    
    print(stages[lives])
    position = 0
    print(f"{' '.join(display)}") # print(display)

    if "_" not in display:
        print("You win!")



#Check guessed letter
# for position in range(word_length):
#     letter = chosen_word[position]
#     print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")

#     if letter == guess:
#         display[position] = letter

# print(display)