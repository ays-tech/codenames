# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

prompt = True


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetics():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print('An illegal character was entered please provide letters only')
        generate_phonetics()
    else:
        print(output_list)


generate_phonetics()

while prompt:
    answer = input('do you want to continue getting code names "YES/No"').lower()
    if answer == 'yes':
        generate_phonetics()
    elif answer == 'no':
        print('see you soon')
        break
    else:
        print('not recognisable')