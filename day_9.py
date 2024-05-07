# programming_dictionary = {
#   "Bug": "An error in a program that prevents the program from running as expected.", 
#   "Function": "A piece of code that you can easily call over and over again."}

# # Retriveing items from the dictionary
# # print(programming_dictionary["Bug"])

# # Adding new items to the dictionary
# programming_dictionary["Loop"] = "The action of doing something over and over again."

# # print(programming_dictionary)

# # Create an empty dictionary
# empty_dictionary = {}

# # Wipe an existing dictionary
# # programming_dictionary = {}
# # print(programming_dictionary)

# # Edit an item in a dictionary
# programming_dictionary["Bug"] = "A moth in your computer."
# # print(programming_dictionary["Bug"])
# # print(programming_dictionary)

# # Loop through a dictionary
# for key in programming_dictionary:
#   print(key)
#   print(programming_dictionary[key])

# day-9 Exercise - 1
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆
# # TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}

# # TODO-2: Write your code below to add the grades to student_grades.👇
# for student in student_scores:
#   score = student_scores[student]
#   # print(score)
#   if score > 90:
#     student_grades[student] = "Outstanding"
#   elif score > 80:
#     student_grades[student] = "Exceeds Expectations"
#   elif score > 70:
#     student_grades[student] = "Acceptable"
#   else:
#     student_grades[student] = "Fail"

# # 🚨 Don't change the code below 👇
# print(student_grades)

# ================================================================
# Nesting 
# capitals ={
#   "France": "Paris",
#   "Germany": "Berlin"
# }

# # Nesting a list in a dictionary
# travel_log = {
#   "France": ["Paris", "Lille", "Dijon"],
#   "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }

# # Nesting a dictionary in a dictionary
# travel_log = {
#   "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#   "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
# }

# # Nesting a dictionary in a list
# travel_log = [
#   {
#     "Country": "France", 
#     "cities_visited": ["Paris", "Lille", "Dijon"], 
#     "total_visits": 12
#   },
#   {
#     "Country": "Germany", 
#     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#     "total_visits": 5
#   }
# ]

# day-9 Exercise - 2
country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 

def add_new_country(country, visits, list_of_cities):
  travel_log.append({"country": country, "visits": visits, "cities": list_of_cities})
  # can also be written as
  # new_country = {}
  # new_country["country"] = name
  # new_country["visits"] = times_visited
  # new_country["cities"] = cities_visited
  # travel_log.append(new_country)

# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
