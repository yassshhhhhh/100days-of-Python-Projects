#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to tip calculator!")

Initial_bill = float(input("What was the total bill? $"))
Tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
Number_of_people = int(input("How many people to split the bill? "))

Tip_value = (Tip_percentage * Initial_bill) / 100
Total_bill = Initial_bill + Tip_value
bill_per_person = Total_bill / Number_of_people
final = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${final}")