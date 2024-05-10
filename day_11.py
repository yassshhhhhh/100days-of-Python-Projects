import random

def add(n1, n2):
    return n1 + n2

def random_card(cards):
    return random.choice(cards)

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

game = True
while game is True:
    play = input("Do you want to play 'Black Jack'? Type 'y' or 'n': ").lower()
    ran_card_1 = random_card(deck)
    ran_card_2 = random_card(deck)
    user_total = add(ran_card_1, ran_card_2)
    coms_ran_card_1 = random_card(deck)
    coms_ran_card_2 = random_card(deck)
    computer_total = add(coms_ran_card_1, coms_ran_card_2)
    if play == "y":
        print(f"Your cards: [{ran_card_1}, {ran_card_2}], Current score: {user_total}")
        print(f"Computer's first card: {coms_ran_card_1}")
        next_turn = input("Type 'y' to get another card, type 'n' to pass: ")
        if next_turn == 'y':
            ran_user_card = random_card(deck)
            user_total = add(user_total, ran_user_card)
            print(f"Your cards: [{ran_card_1}, {ran_card_2}, {ran_user_card}], Current score: {user_total}")
            ran_comps_card = random_card(deck)
            computer_total = add(computer_total, ran_comps_card)
            print(f"Computer's first card: {coms_ran_card_1}")
            if user_total <= 21 and computer_total <= 21:
                if user_total > computer_total:
                    print(f"Your final hand: [{ran_card_1}, {ran_card_2}, {ran_user_card}], final score: {user_total}")
                    print(f"Computer's final hand[{coms_ran_card_1}, {coms_ran_card_2}, {ran_comps_card}], final score: {computer_total}")
                    print("You win!")
                elif user_total < computer_total:
                    print(f"Your final hand: [{ran_card_1}, {ran_card_2}, {ran_user_card}], final score: {user_total}")
                    print(f"Computer's final hand[{coms_ran_card_1}, {coms_ran_card_2}, {ran_comps_card}], final score: {computer_total}")
                    print("You Lose!")
                else:
                    print(f"Your final hand: [{ran_card_1}, {ran_card_2}, {ran_user_card}], final score: {user_total}")
                    print(f"Computer's final hand[{coms_ran_card_1}, {coms_ran_card_2}, {ran_comps_card}], final score: {computer_total}")
                    print("It's a draw!")
            elif user_total <= 21 and computer_total > 21:
                print(f"Your final hand: [{ran_card_1}, {ran_card_2}, {ran_user_card}], final score: {user_total}")
                print(f"Computer's final hand[{coms_ran_card_1}, {coms_ran_card_2}, {ran_comps_card}], final score: {computer_total}")
                print("Opponent went over. You win!")
            elif user_total > 21 and computer_total <= 21:
                print(f"Your final hand: [{ran_card_1}, {ran_card_2}, {ran_user_card}], final score: {user_total}")
                print(f"Computer's final hand[{coms_ran_card_1}, {coms_ran_card_2}, {ran_comps_card}], final score: {computer_total}")
                print("You went over. You lose!")
            else:
                print(user_total)
                print(computer_total)
        elif next_turn == 'n':
            # print(f"Your cards: [{ran_card_1}, {ran_card_2}], Current score: {user_total}")
            ran_comps_card = random_card(deck)
            computer_total = add(computer_total, ran_comps_card)
            if user_total <= 21 and computer_total <= 21:
                if user_total > computer_total:
                    print(f"Your final hand: [{ran_card_1}, {ran_card_2}], final score: {user_total}")
                    print(f"Computer's final hand[{coms_ran_card_1}, {coms_ran_card_2}, {ran_comps_card}], final score: {computer_total}")
                    print("You win!")
                elif user_total < computer_total:
                    print(f"Your final hand: [{ran_card_1}, {ran_card_2}], final score: {user_total}")
                    print(f"Computer's final hand[{coms_ran_card_1}, {coms_ran_card_2}, {ran_comps_card}], final score: {computer_total}")
                    print("You Lose!")
                else:
                    print(f"Your final hand: [{ran_card_1}, {ran_card_2}], final score: {user_total}")
                    print(f"Computer's final hand[{coms_ran_card_1}, {coms_ran_card_2}, {ran_comps_card}], final score: {computer_total}")
                    print("It's a draw!")
            elif user_total > 21 and computer_total <= 21:
                print(f"Your final hand: [{ran_card_1}, {ran_card_2}, {ran_user_card}], final score: {user_total}")
                print(f"Computer's final hand[{coms_ran_card_1}, {coms_ran_card_2}, {ran_comps_card}], final score: {computer_total}")
                print("You went over. You lose!")
            elif computer_total > 21 and user_total <= 21:
                print(f"Your final hand: [{ran_card_1}, {ran_card_2}], final score: {user_total}")
                print(f"Computer's final hand[{coms_ran_card_1}, {coms_ran_card_2}, {ran_comps_card}], final score: {computer_total}")
                print("Opponent went over. You win!")
            else:
                print(user_total)
                print(computer_total)
    else:
        game = False
        print("Goodbye.")
