################### Scope ####################

# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# local scope

# def drink_potion():
#   potion_strength = 2
#   print(potion_strength)

# drink_potion()
# print(potion_strength)

# global scope
# player_health = 10 #global scope

# def drink_potion():
#   potion_strength = 2 #local scope
#   print(player_health)

# drink_potion()
# print(player_health)

# there is no block scope
# game_level = 3

# def game():
#   enemies = ["skeleton", "zombie", "alien"]
#   if game_level < 5:
#     game_level = enemies[0]
#   # else:
#   #   game_level = enemies[1]
#     print(game_level)

# Modifying global scope

# enemies = 1
# print(enemies)
# def increase_enemies():
#   # global enemies #global scope statement. But it is fallible. So rather than modifying global scope, we can use the return statement.
#   print(f"enemies inside function: {enemies}")
#   return enemies + 1

# enemies = increase_enemies()
# print(f"enemies outside function: {enemies}")

# Global constants
# PI = 3.14159
# URL = "https://www.google.com"
# TWITTER_HANDLE = "@yassshhhhh"

def bar():
    my_variable = 9

    if 16 > 9:
      my_variable = 16

    print(my_variable)
    # Remember that in Python there is no block scope. Inside a if/else/for/while code block is the same as outside it.

bar()