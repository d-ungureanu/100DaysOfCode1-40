numbers = [1, 2, 3, 4]
new_list = []
for number in numbers:
    add_1 = number + 1
    new_list.append(add_1)
print(new_list)

# List comprehension
# new_list = [new _item for item in list]

new_list_2 = [number + 1 for number in numbers]
print(new_list_2)

name = "Daniel"

name_list = [letter for letter in name]
print(name_list)

numbers_list = [n * 2 for n in range(1, 5)]
print(numbers_list)
