logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

anybody_else = 'y'
players = {}


def winner(players):
    winner = 0
    winner_name = ""
    for bid in players:
        amount = players[bid]
        if (amount > winner):
            winner = amount
            winner_name = bid
    print(f"The winner is {winner_name} with a bid of {winner}")


while(anybody_else == 'y'):
    name = input("Participant's name: ")
    bid = float(input("How much this participant want to bid: "))
    players[name] = bid
    anybody_else = input(
        "There is somebody else to give a bid? 'y' or 'n' ").lower()

winner(players)
