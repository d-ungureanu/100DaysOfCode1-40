import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
# Lopping through dictionaries:
# for (key, value) in student_dict.items():
#     print(value)

# Create data frame from dictionary
student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# # Loop through a data frame
# for (key, value) in student_data_frame.items():
#     print(value)


# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(row.score)
