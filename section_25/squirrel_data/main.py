import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color_column = data["Primary Fur Color"]
color_count = color_column.value_counts()
# color_column.value_counts().to_csv("unique_colors_count.csv", header=["Fur Color", "Count"])
print(color_count)
gray_s_count = color_count[0]
red_s_count = color_count[1]
black_s_count = color_count[2]
print(gray_s_count)
print(red_s_count)
print(black_s_count)
data_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [gray_s_count, red_s_count, black_s_count]
}

pandas.DataFrame(data_dict).to_csv("s_count_by_colors.csv")