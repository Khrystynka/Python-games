import pandas
data = pandas.read_csv('nato_alphabet/nato_phonetic_alphabet.csv')
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
user_input = input('Please enteryout word: ')
result = [nato_dict[x] for x in user_input.upper()]
print(result)
