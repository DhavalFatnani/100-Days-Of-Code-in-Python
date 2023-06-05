import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
dictionary = {row.letter: row.code for (index, row) in df.iterrows()}
word = input("Enter the Word: ").upper()
nato_words_list = [dictionary[letter] for letter in word]
print(nato_words_list)
