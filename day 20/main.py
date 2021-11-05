# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

template = open("./Input/Letters/starting_letter.txt").read()
names = open("./Input/Names/invited_names.txt").readlines()

PLACEHOLDER = "[name]"

for name in names:
    name_clean = name.strip()
    letter = open(f"./Output/ReadyToSend/letter_for_{name_clean}", mode="w")
    letter.write(template.replace(PLACEHOLDER, name_clean))
