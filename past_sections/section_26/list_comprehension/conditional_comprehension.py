# Conditional List Comprehension
# new_list = [new_item for item in list if test]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

short_names_list = [name for name in names if len(name) < 5]
print(short_names_list)

"text".upper()
upper_case_names = [name.upper() for name in names if len(name) > 4]
print(upper_case_names)
