import random
word_list = ["Java", "Python", "JavaScript"]

random_word = random.choice(word_list)

display = []
for rw in random_word:
    display += "_"
print(display)

letter = input("Guess a letter: ").lower()


quantity = 0
for rw in random_word:
    if(rw == letter):
        quantity += 1
