# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# def greet():
#   print("Hello!")
#   print("How are you?")
#   print("Isn't the weather nice today?")

# greet()

# def greet_with_name(name):
#   print(f"Hello {name}!")
#   print(f"How are you {name}?")

# # name is a parameter and input is an argument

# greet_with_name(input("What is your name? "))

def greet_with(name, location):
  print(f"Hello {name}!")
  print(f"What is it like in {location}?")

# positional arguments
# greet_with("Yash", "India")")

# keyword arguments
greet_with(location = "Konoha", name = "Itachi")

# name = input("What is your name? ")
# location = input("Where are you from? ")
# greet_with(name, location)


# Function for Prime number checker:
# Write your code below this line 👇

def prime_checker(number):
  count = 0
  for num in range(1, number + 1):
    # print(num)
    if number % num == 0:
      count += 1
      # print(count)
  if count > 2:
    print("It's not a prime number.")
  else:
    print("It's a prime number.")

# Can also be written as:
#   is_prime = True
#   for i in range(2, number):
#     if number % i == 0:
#       is_prime = False
#   if is_prime:
#     print("It's a prime number.")
#   else:
#     print("It's not a prime number.")
   
# Write your code above this line 👆
    
#Do NOT change any of the code below👇

n = int(input("Enter a number: ")) # Check this number
prime_checker(number=n)