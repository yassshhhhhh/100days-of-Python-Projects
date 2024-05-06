#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letters, 2 symbols, 2 numbers = JduE&!91

password = []

for i in range(0,nr_letters):
  random_letter = random.randrange(0,len(letters)-1)
  password.append(letters[random_letter])
# print(final_letters)

for i in range(0,nr_symbols):
  random_symbol = random.randrange(0,len(symbols)-1)
  password.append(symbols[random_symbol])
# print(final_symbols)

for i in range(0,nr_numbers):
  random_number = random.randrange(0,len(numbers)-1)
  password.append(numbers[random_number])
# print(final_numbers)

# print(password)
print("Your Easy-password: ")

for i in password:
  print(i,end="")


#Hard Level - Order of characters randomized:
#e.g. 4 letters, 2 symbols, 2 numbers = g^2jk8&P
print("\nYour Hard-password:")
hard_password = password

random.shuffle(hard_password)

for i in hard_password:
  print(i, end="")

print(" ")


# #Eazy Level
# # password = ""

# # for char in range(1, nr_letters + 1):
# #   password += random.choice(letters)

# # for char in range(1, nr_symbols + 1):
# #   password += random.choice(symbols)

# # for char in range(1, nr_numbers + 1):
# #   password += random.choice(numbers)

# # print(password)

# #Hard Level
# password_list = []

# for char in range(1, nr_letters + 1):
#   password_list.append(random.choice(letters))

# for char in range(1, nr_symbols + 1):
#   password_list += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password_list += random.choice(numbers)

# print(password_list)
# random.shuffle(password_list)
# print(password_list)

# password = ""
# for char in password_list:
#   password += char

# print(f"Your password is: {password}")