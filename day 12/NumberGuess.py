import random

# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
print("Welcome to guessing game!\nI'm thinking of a number between 1 and 100")
random_number = random.randint(1, 100)
is_game_over = False
difficulty = input(
    "Please, choose a difficulty. Type 'easy' or 'hard': ").lower()


def guess(number):
    if (number > random_number):
        print("Too high 🚨. Guess again")
    elif(number < random_number):
        print("Too low 🚨. Guess again")
    else:
        print("You win!🎉🎉")
        global is_game_over
        is_game_over = True


def game(attempts):
    while((attempts > 0) and (not is_game_over)):
        print(f"You have {attempts} attempts remaining to guess the number.")
        number = int(input("Make a guess: "))
        guess(number)
        attempts -= 1
    if(attempts == 0):
        print(f"You lose, the number was {random_number} ⚰️")


if (difficulty == "easy"):
    game(10)
else:
    game(5)
