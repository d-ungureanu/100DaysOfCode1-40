# with open("weather_data.csv", "r") as weather_file:
#     data = weather_file.read().splitlines()
# print(data)


# import csv
# with open("weather_data.csv", "r") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     print(data)
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
import statistics

import pandas
import pprint

data = pandas.read_csv("weather_data.csv")
# temps = data["temp"]
# print(data.columns)
# temperatures = list(temps)
# print(temperatures)
# data_dict = data.to_dict()
# pprint.pprint(data_dict)

# average_temp = temps.mean()
# print("The average temperature is: {:.2f}".format(average_temp))
# print(f"The max temperature is: {temps.max()}")

# # Get data in columns
# print(data.day)
# print(data["day"])

# Get data in Rows
# All days with 14 degrees
# print(data[data.temp == 14])

# Day with the highest temp
# highest_temp = data.temp.max()
# print(data[data.temp == highest_temp])

# Highest Celsius converted to Fahrenheit
# highest_temp = data.temp.max()
# highest_temp_row = data[data.temp == highest_temp]
# temp_in_C = int(highest_temp_row.temp)
# temp_in_F = (temp_in_C * 9 / 5) + 32
# print(f"Temperature in Fahrenheit: {temp_in_F}")


# Create dataframe from scratch
data_dict = {
    "students": ["Daniel", "Silvia", "Mimi"],
    "grades": [76, 82, 65]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_csv_data.csv")
