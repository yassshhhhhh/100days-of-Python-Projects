from day_14_data import data
import random

def game(question_A, question_B):
    print(f"Compare A: {question_A['name']}, a {question_A['description']}, from {question_A['country']}")
    A = question_A['follower_count']
    print(""" 
        __   __   ___   
        \ \ / /  / __|  
        \ V /   \__ \  
        _\_/_   |___/  
        _| """"|_|"""""| 
        "`-0-0-'"`-0-0-' 
    """)
    print(f"Against B: {question_B['name']}, a {question_B['description']}, from {question_B['country']}")
    B = question_B['follower_count']
    if A > B:
        act_ans = A
        return act_ans
    else:
        act_ans = B
        return act_ans

# def compare(act_ans):
#     if act_ans == foll_count:
#         score += 1
#         print(f"You're right! Current score: {score}.")
#         return 1
#     else:
#         print(f"Sorry, that's wrong. Final score: {score}.")
#         return 0
    
    
# def compare(Ques_a, Ques_b):
#     if Ques_a['follower_count'] > Ques_b['follower_count']:
#         game()
score = 0
game_is = True
while game_is is True:
    question_A = random.choice(data)
    question_B = random.choice(data)
    # game(question_A, question_B)
    if question_A != question_B:
        act_ans = game(question_A, question_B)
        print(act_ans)
        ans = input("Who has more followers? Type 'A' or 'B': ").lower()
        if ans == "a":
            foll_count = question_A['follower_count']
            print(foll_count)
        elif ans == "b":
            foll_count = question_B['follower_count']
            print(foll_count)
        # final = compare(act_ans)
        if act_ans == foll_count:
            score += 1
            print(f"You're right! Current score: {score}.")
            final = 1
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            final = 0

        if final == 0:
            game_is = False