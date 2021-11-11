import random
from data import data
from logo import vs, logo
from os import system

compareA = []
compareB = []
followersA = ""
followersB = ""
points = 0
winner = ""
guess = ""


def people():
    global compareA, compareB, followersA, followersB
    compareA = random.choice(data)
    compareB = random.choice(data)
    followersA = compareA['follower_count']
    followersB = compareB['follower_count']


if(followersA > followersB):
    winner = "a"
else:
    winner = "b"


def game():
    people()
    print(logo)
    if(points != 0):
        print(f"You're right! Current score {points}")
    print(
        f"Compare A: {compareA['name']}, a {compareA['description']}, from {compareA['country']}")
    print(vs)
    print(
        f"Against B: {compareB['name']}, a {compareB['description']}, from {compareB['country']}")
    global guess
    guess = str(input("Who has more followers? Type A or B: ")).lower()
    while(guess != "a" and guess != "b"):
        guess = str(
            input("Invalid input. Who has more followers? Type A or B: ")).lower()


game()
while (guess == winner):
    points += 1
    _ = system("clear")
    game()

print(f"You lose! You're score was {points}")
