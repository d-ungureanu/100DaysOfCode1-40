with open("file1.txt", "r") as file_1:
    file_1_data = file_1.read().splitlines()
with open("file2.txt", "r") as file_2:
    file_2_data = file_2.read().splitlines()
print(file_1_data)
print(file_2_data)
new_list = [number for number in file_1_data if number in file_2_data]
print(new_list)
