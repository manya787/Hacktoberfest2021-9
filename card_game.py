import random

# Define the ranks, suits, and values for a standard deck of cards
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

# Create a deck of cards
deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]

# Shuffle the deck
random.shuffle(deck)

# Function to deal cards to players
def deal_cards(num_players, num_cards):
    players = [[] for _ in range(num_players)]

    for _ in range(num_cards):
        for player in players:
            card = deck.pop()
            player.append(card)

    return players

# Number of players and cards to deal
num_players = 4
num_cards = 5

# Deal cards to players
players = deal_cards(num_players, num_cards)

# Display the hands of each player
for i, player in enumerate(players):
    print(f"Player {i + 1}'s Hand:")
    for card in player:
        print(f"{card['rank']} of {card['suit']}")
    print()
