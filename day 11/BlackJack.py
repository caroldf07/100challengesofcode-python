import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

print(logo)
game_play = input(
    "Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

player_cards = []
computer_cards = []
game_over = False


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):

    if (sum(cards) == 21) and (len(cards) == 2):
        return 0

    if(11 in cards) and (sum(cards) > 21):
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(player_score, computer_score):
    if (player_score == computer_score):
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack!"
    elif player_score == 0:
        return "Win with a Blackjack :D"
    elif player_score > 21:
        return "You lose. Game over!"
    elif computer_score > 21:
        return "You win!!"
    elif player_score > computer_score:
        return "You win!!"
    else:
        return "You lose. Game over!"


for _ in range(2):
    player_cards.append(deal_card())
    computer_cards.append(deal_card())

while not game_over:
    player_score = calculate_score(player_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(
        f"Computer's cards: {computer_cards}, current score: {computer_score}")

    if (player_score == 0) or (computer_score == 0) or (player_score > 21):
        game_over = True
    else:
        if(input("Type 'y' to get another card, type 'n' to pass: ").lower() == 'y'):
            player_cards.append(deal_card())
        else:
            game_over = True

while (computer_score != 0) and (computer_score < 17):
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

print(compare(player_score, computer_score))
