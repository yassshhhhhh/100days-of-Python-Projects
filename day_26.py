# student_dict = {
#     "student": ["Maya", "Itachi", "Yash"],
#     "score": [99, 97, 80]
# }

# # for (key, value) in student_dict.items():
#     # print(value)

# import pandas

# new_data = pandas.DataFrame(student_dict)
# # print(new_data)

# # Loop through a dataframe
# # for (key, value) in new_data.items():
# #     print(value)

# # Loop through rows of dataframe
# for (index, row) in new_data.iterrows():
#     # print(index)
#     # print(row.student)
#     if row.score > 97:
#         print(f"{row.student} is the topper with a score of {row.score}.")

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(type(data))
dict_data = {row.letter: row.code for (index, row) in data.iterrows()}
print(dict_data)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("Enter you name: ").upper()
letters_list = [dict_data[letter] for letter in user_input]
print(letters_list)
