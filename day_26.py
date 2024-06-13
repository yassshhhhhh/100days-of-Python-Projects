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
