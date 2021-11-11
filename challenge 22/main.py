import pandas

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
phonetic_dict = {row.letter: row.code for (index, row) in alphabet.iterrows()}

word = input("Enter a word: ").upper()
output = []

for letter in word:
    output.append(phonetic_dict[letter])

print(output)

##A clenear way to do the same thing

output2 = [phonetic_dict[letter] for letter in word]
print(output2)
