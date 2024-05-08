# Using clear function to clear the output


dict_bid = {}
highest_bid = 0
def bid_users():
    name = input("What is your name? ")
    bid = int(input("What is your bid?: $"))
    dict_bid[name] = bid

bid_users()

users = True

while users is True:
    new_user = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
    if new_user == "yes":
        # Use clear function here.
        print("Clear")
        bid_users()
    elif new_user == "no":
        users = False
        for users in dict_bid:
            if dict_bid[users] > highest_bid:
                highest_bid = dict_bid[users]
        print(f"The winner is {users} with a bid of ${highest_bid}")
    else:
        print("Enter a valid input.")



# print(dict_bid)