"""
Class Summary :

Player constructor get:

name - The player name.

card_counter - Initialized by `default` The player who won the round his own card_counter + 1.

cards - Array that have all the player cards after sharing the cards to players

add_card - function that add card to cards player array

"""


class Player:

    def __init__(self, name):
        self.name = name
        self.round_counter = 0
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)
