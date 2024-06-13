# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temp = int(row[1])
#             temperatures.append(temp)
#     print(temperatures)

        # temperatures.pop(0)
        # new_temps = []
        # for temps in temperatures:
        #     temps = int(temps)
        #     new_temps.append(temps)
        # print(new_temps)
        # print(data)


# import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))
# for temp in data["temp"]:
#     print(temp)

# data_dict = data.to_dict()
# # print(data_dict)
# temp_list = data["temp"].to_list()
# print(temp_list)

# total_temp = 0
# for temp in temp_list:
#     total_temp += temp
#
# average_temp = total_temp/len(temp_list)
# print(average_temp)

# average_temp = data["temp"].mean()  # Above comment line's code is equal to this single line of code.
# print(average_temp)
#
# max_temp = data["temp"].max()
# print(max_temp)


# Get Data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# cel_temp = monday.temp[0]
# fahrenheit = (cel_temp*(9/5)) + 32
# print(fahrenheit)

# Create dataframe from scratch
# data_dict = {
#     "students": ["Yash", "Ashwin", "Tarun"],
#     "Scores": [80, 95, 70]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# 
# data_names = data["students"]
# # print(data_names)
# # print(data[data.students == "Yash"])
# for i in range(len(data.Scores)):
#     print(data.Scores[i])
# -------------------------------------------------------------
# Squirrel_data_file
# import pandas

# data = pandas.read_csv("squirrel.csv")
# count_grey = len(data[data["Primary Fur Color"] == "Gray"])
# count_red = len(data[data["Primary Fur Color"] == "Cinnamon"])
# count_black = len(data[data["Primary Fur Color"] == "Black"])
# print(count_grey, count_red, count_black)

# data_dict = {
#     "Fur color" : ["Gray", "Cinnamon", "Black"],
#     "Count" : [count_grey, count_red, count_black]
# }

# new_data = pandas.Dataframe(data_dict)
# new_data.to_csv("color_data.csv")
# print(new_data)
# --------------------------------------------------------------
