from day_14_data import data
import random

def game(question_A, question_B):
    print(f"Compare A: {question_A['name']}, a {question_A['description']}, from {question_A['country']}")
    A = question_A['follower_count']
    print("""   
         _  _____
        | |/ (_-<
        |___/___/
    """)
    print(f"Against B: {question_B['name']}, a {question_B['description']}, from {question_B['country']}")
    B = question_B['follower_count']
    if A > B:
        act_ans = A
        return act_ans
    else:
        act_ans = B
        return act_ans

score = 0
game_is = True
print(""" 
   __ ___      __          
  / // (_)__ _/ /  ___ ____
 / _  / / _ `/ _ \/ -_) __/
/_//_/_/\_, /_//_/\__/_/   
     __/___/__             
    / _ \/ __/             
   _\___/_/                
  / /__ _    _____ ____    
 / / _ \ |/|/ / -_) __/    
/_/\___/__,__/\__/_/                                                                                                                                                               
""")
question_A = random.choice(data)
question_B = random.choice(data)
if question_A == question_B:
    question_B = random.choice(data)
while game_is is True:
    act_ans = game(question_A, question_B)
    # print(act_ans)
    ans = input("Who has more followers? Type 'A' or 'B': ").lower()
    if ans == "a":
        foll_count = question_A['follower_count']
        # print(foll_count)
    elif ans == "b":
        foll_count = question_B['follower_count']
        # print(foll_count)
    # clear()
    # print(logo)
    if act_ans == foll_count:
        score += 1
        print(f"You're right! Current score: {score}.")
        final = 1
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        final = 0
    question_A = question_B
    question_B = random.choice(data)
    if final == 0:
        game_is = False