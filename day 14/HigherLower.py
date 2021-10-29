import random
from data import data
from logo import vs, logo

compareA = random.choice(data)
compareB = random.choice(data)
points = 0

print(logo)
print(
    f"Compare A: {compareA['name']}, a {compareA['description']}, from {compareA['country']}")
print(vs)
print(
    f"Against B: {compareB['name']}, a {compareB['description']}, from {compareB['country']}")
guess = str(input("Who has more followers? Type A or B: ")).lower()
