
class Player:

    def __init__(self, name):
        """
        :param
        name: The player name.
        win_card_counter - Initialized by `default` The player who won the round his own card_counter + 1.
        cards - Array that have all the player cards after sharing the cards to players
        """
        self.name = name
        self.win_round_counter = 0
        self.cards = []

    def add_card(self, card):
        """
        :param card: card we want to add
        :return:  card to cards player array
        """
        self.cards.append(card)
