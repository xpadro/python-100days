student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# {"A": "Alfa", "B": "Bravo"}
alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
letter_code_pairs = {row.letter: row.code for (index, row) in alphabet.iterrows()}


def generate_code():
    word = input("Enter a word: ").upper()
    try:
        result = [letter_code_pairs[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet")
        generate_code()
    else:
        print(result)


generate_code()
