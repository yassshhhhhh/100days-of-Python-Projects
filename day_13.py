############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

# def my_function():
#   for i in range(1, 21): #range function doesn't include target range.
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5) #randint includes both parameters.
# print(dice_imgs[dice_num]) #we are returning.

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# year = int(input("What's your year of birth?"))
# if year > 1980 and year <= 1994: # '=' is required to assing if the existing year is in millenial or not.
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# age = input("How old are you?") # It returns values as string.
# if age > 18:
# print("You can drive at age {age}.")

# age = int(input("How old are you?")) # Now it returns values as integer.
# if age > 18:
#     print(f"You can drive at age {age}.") # requires indentation and 'f' string.

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: ")) #'==' is assingment operator and "=" is equals to
# total_words = pages * word_per_page
# print(pages)
# print(word_per_page)
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])

def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item) # Requires indentation for every number to append in the list while it's multiplying by 2.
  print(b_list)

mutate([1,2,3,5,8,13])
