# Defining the function

def my_function():
  print("Hello!")
  print("Bye!")

# Calling the function
my_function()

def counting_nums():
  for num in range(1,11):
    print(num)
  print("The total number of digits in the number are:", num)

counting_nums()

# def turn_right():
#   turn_left()
#   turn_left()
#   turn_left()

# def rep_action():
#   move()
#   turn_left()
#   move()
#   turn_right()
#   move()
#   turn_right()
#   move()
#   turn_left()

# num_of_jumps = 0
# while at_goal() is False:
#   rep_action()
#   num_of_jumps += 1
#   print(num_of_jumps)


# ===============================================================
# #while not at_goal():
#   #rep_action()

# #while at_goal() != True:
#   #rep_action


# ===============================================================
# while not at_goal():
#   if wall_in_front():
#       rep_action()
#   else:
#       move()

# ===============================================================

# while at_goal() is False:
#   if right_is_clear():
#       turn_right()
#       move()
#   elif front_is_clear():
#       move()
#   elif wall_in_front():
#       turn_left()
#   else:
#       rep_action()

# ===============================================================
# def turn_right():
#   turn_left()
#   turn_left()
#   turn_left()

# def rep_action():
#   turn_left()
#   while wall_on_right():
#       move()
#   turn_right()
#   move()
#   turn_right()
#   while front_is_clear():
#       move()
#   turn_left()

# while at_goal() is False:
#   if wall_in_front():
#       rep_action()
#   else:
#       move()

# ===============================================================
# This is the project related to the maze, Where the robot finds his way out.

# Link: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# My Solution
# def turn_right():
#   turn_left()
#   turn_left()
#   turn_left()

# while not at_goal():
#   if right_is_clear():
#       turn_right()
#       move()
#   elif front_is_clear() is False:
#       turn_left()
#   else:
#       move()

# Also can be written as
    # elif front_is_clear():
    #     move()
    # else:
    #     turn_left()
