import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Loop through rows of a data frame
nato_alpha_dict = {row.letter: row.code for (index, row) in data.iterrows()}


user_input = input("Please enter the word: ").upper()
nato_phonetic_list = [nato_alpha_dict[letter] for letter in user_input]
print(nato_phonetic_list)
