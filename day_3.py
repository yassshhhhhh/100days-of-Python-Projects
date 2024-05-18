# It has multiple mini projects to understand basic concepts.

# # Rollercoaster Ride
# print("Welcome to the rollercoaster!")
# height1 = int(input("What is your height in cm? "))
# bill = 0

# if height1 >= 120:
#   print("You can ride Rollercoaster!")
#   age  = int(input("Enter your age: "))
#   if age < 12:
#     bill = 5
#     print("Child tickets are $5")
#   elif age <= 18:
#     bill = 7
#     print("Youth tickets are $7")
#   elif age >= 45 and age <= 55:
#     print("You can ride for free")
#   else:
#     bill = 12
#     print("Adult tickets are $12")
#   photo = input("Do you want to take photo? Yes or No: ")
#   if photo.lower() == "yes":
#     bill += 3
#   print(f"Your total bill is ${bill}")
# else:
#   print("Sorry, You have to grow taller to ride Rollercoaster.")

# # Even or Odd
# number = int(input("Enter a number: "))

# if number % 2 == 0:
#   print("Entered number is even!")
# else:
#   print("Entered number is odd!")

# #BMI Calculator
# height = float(input("Enter your height in meters(m): "))
# weight = float(input("Enter your weight in kilogram(kg): "))

# BMI = round(weight / (height**2), 2)

# if BMI < 18.5:
#   print(f"Your BMI is {BMI}, you are underweight.")
# elif BMI < 25:
#   print(f"Your BMI is {BMI}, you are healthyweight.")
# elif BMI < 30:
#   print(f"Your BMI is {BMI}, you are overweight.")
# elif BMI < 35:
#   print(f"Your BMI is {BMI}, you are obese.")
# else: 
#   print(f"Your BMI is {BMI}, you are clinically obese.")

# #Leap Year
# year  = int(input("Enter a year: "))

# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Entered year is a leap year!")
#     else:
#       print("Entered year is not a leap year!")
#   else:
#     print("Entered year is a leap year!")
# else:
#   print("Entered year is not a leap year!")

# # Pizza order
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size of pizza do you want? S, M or L: ")
# add_pepperoni = input("Do you want pepperoni? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")

# bill = 0

# if size == "S":
#   bill += 15
# elif size == "M":
#   bill += 20    
# else:
#     bill += 25

# if add_pepperoni == "Y":
#   if size == "S":
#     bill += 2
#   else:
#     bill += 3
    
# if extra_cheese == "Y":
#   bill += 1

# print("Thankyou for choosing Python Pizza deliveries.")
# print(f"Your final bill is ${bill}.")


# Love Calculator
print("The love calculator is calculating your score...!")
name1 = input("Enter your name: ").lower()
name2 = input("Enter your partner name: ").lower()

combined_name = name1 + name2

t = int(combined_name.count("t"))
r = int(combined_name.count("r"))
u = int(combined_name.count("u"))
e = int(combined_name.count("e"))
true = t + r + u + e
l = int(combined_name.count("l"))
o = int(combined_name.count("o"))
v = int(combined_name.count("v"))
e = int(combined_name.count("e"))
love = l + o + v + e
love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
  print(f"Your love score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
  print(f"Your love score is {love_score}, you are alright together.")
else:
  print(f"Your love score is {love_score}.")