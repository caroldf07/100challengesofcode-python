import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
hand = [rock, paper, scissors]


again = "yes"

while(again == "yes"):
    player = int(
        input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors: "))

    computer = random.choice(hand)

    if(player == 0 and computer == rock):
        again = input(f"{rock}\nIt's a draw! Play again, yes or no? ")
    elif(player == 0 and computer == paper):
        again = input(f"{paper}\nYou loose! Play again, yes or no? ")
    elif(player == 0 and computer == scissors):
        again = input(f"{scissors}\nYou win! Play again, yes or no? ")
    elif(player == 1 and computer == paper):
        again = input(f"{paper}\nIt's a draw! Play again, yes or no? ")
    elif(player == 1 and computer == scissors):
        again = input(f"{scissors}\nYou loose! Play again, yes or no? ")
    elif(player == 1 and computer == rock):
        again = input(f"{rock}\nYou win! Play again, yes or no? ")
    elif(player == 2 and computer == scissors):
        again = input(f"{scissors}\nIt's a draw! Play again, yes or no? ")
    elif(player == 2 and computer == rock):
        again = input(f"{rock}\nYou loose! Play again, yes or no? ")
    elif(player == 2 and computer == paper):
        again = input(f"{paper}\nYou win! Play again, yes or no? ")
    else:
        again = input("Invalid choice! Try again, yes or no? ")
