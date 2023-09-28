import pandas as pd

#TODO 1. Create a dictionary in this format:
df=pd.read_csv("nato_phonetic_alphabet.csv")
dict={row.letter: row.code for (index,row) in df.iterrows()}
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def phonetic_word_list(input: str):
    try:
        return [dict[char.upper()] for char in input]
    except KeyError:
        return "Sorry, only letters in the alphabet please"

input_str= input()
print(phonetic_word_list(input_str))