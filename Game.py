from CardGame.Card import Card
import random

from CardGame.Player import Player
from CardGame.constants import MENU_CONTENT, START_GAME, FIRST_PLAYER, SECOND_PLAYER, TIE, PLAYER_CARDS, \
    SAME_CARD_NUMBER, SHAPES, NUMBERS, MIN, FIRST_MIDDLE, SECOND_MIDDLE, MAX, ROUND_RESULT_MESSAGE, WIN_ROUND_MESSAGE, \
    PLAYER_CARDS_HEADER_MESSAGE, WINNER_MESSAGE


class Game:
    shape_dict_number = {"♥": 1, "♠": 2, "♦": 3, "♣": 4}
    shape_dict_royal_card = {"Prince": MIN, "Queen": FIRST_MIDDLE, "King": SECOND_MIDDLE, "Ace": MAX}

    def __init__(self):
        self.deck_array = self.generate_cards()
        self.player1 = None
        self.player2 = None

    @staticmethod
    def generate_cards():
        """
        :return: New cards list that create Cards with number from numbers list and shape from shapes list.
        *Note - WHEN YOU CRATE CARD, CARD CLASS PRINT THE CARD THAT HAS CREATED.
        """
        cards = [Card(number, shape) for number in NUMBERS for shape in SHAPES]

        return cards

    def start(self):
        """
        :return: The game winner with his card counter
        """
        print(MENU_CONTENT)
        self.get_player_names()
        self.distribute_cards()
        self.Validate_same_number_cards()
        self.print_players_cards()
        self.find_round_winner()
        self.find_game_winner()

    def get_player_names(self):
        """
        :return: Get both players names.
        """
        player1_name = input(FIRST_PLAYER)
        self.player1 = Player(player1_name)
        player2_name = input(SECOND_PLAYER)
        self.player2 = Player(player2_name)

    def distribute_cards(self):
        """
        distribute_cards - function that get player1 and player2 and share the cards from deck_array to each player
        list, random.shuffle - mix deck_array. half_size - get length deck_array/2. player1_cards - Creates a list
        containing the first half of the shuffled cards. player2_cards - Creates a list containing the second half of
        the shuffled cards. The two for loops distribute the cards to player1 and player2 by calling the add_card
        method on each player. :return: split the cards list to 2 lists. list for player 1 and list for player 2.
        """
        random.shuffle(self.deck_array)
        half_size = len(self.deck_array) // 2
        self.player1.cards = self.deck_array[:half_size]
        self.player2.cards = self.deck_array[half_size:]

    def Validate_same_number_cards(self):
        """
        :return: Validate both players have same number of cards
        """
        if len(self.player1.cards) != len(self.player2.cards):
            raise ValueError(SAME_CARD_NUMBER)

    def print_players_cards(self):
        """
        :return: Print player cards.
        """
        print(PLAYER_CARDS)
        self.__print_cards(self.player1)
        self.__print_cards(self.player2)

    @staticmethod
    def __print_cards(player):
        """
        :param player:  get player.
        :return: print each card from player cards
        """
        print(PLAYER_CARDS_HEADER_MESSAGE.format(player_name=player.name))
        for card in player.cards:
            print(card)

    def game_rounds(self, card1, card2, game_round):
        """
        :param game_round: The game round, there is 24 rounds.
        :param card1: Calculate the value of the cards1
        :param card2: Calculate the value of the cards2
        :return: The round winner.
        """

        value1 = self.calculate(card2, card1)
        value2 = self.calculate(card1, card2)

        print(ROUND_RESULT_MESSAGE.format(
            game_round=game_round,
            player1_name=self.player1.name,
            card1_number=card1.number,
            card1_shape=card1.shape,
            value1=value1,
            player2_name=self.player2.name,
            card2_number=card2.number,
            card2_shape=card2.shape,
            value2=value2
        ))

        if value1 > value2:
            self.player1.win_round_counter += 1
            print(WIN_ROUND_MESSAGE.format(player_name=self.player1.name, game_round=game_round))
        elif value1 < value2:
            self.player2.win_round_counter += 1
            print(WIN_ROUND_MESSAGE.format(player_name=self.player2.name, game_round=game_round))
        else:
            print(TIE)

    def calculate(self, rival_card, current_card):

        """
        :param current_card: The card current player have.
        :param rival_card: The card the opponent has in the game, we use it to calculate the cards value
        :return:
        if player1 have card with number and player2 have card with number the value
        of the card depend on the card shape :
        Heart - card number multiply by 1.
        Clover - card number multiply by 2.
        Diamond - card number multiply by 3.
        Leaf - card number is multiplied by 4.
        if player1 have royal card and player2 have number card royal card win.
        if player1 have royal card and player2 have royal card King > Queen > Prince
        if player1 number is "Ace" and player2 number is royal card : Ace > King > Queen > Prince
        if player1 number is "Ace" and player2 number is 2-9: return the value of the shape of "Ace"
        """

        # One of the players got Ace
        if current_card.number == "Ace" and rival_card.number in self.shape_dict_royal_card:
            return self.shape_dict_royal_card["Ace"]
        elif current_card.number == "Ace":
            return self.shape_dict_number[current_card.shape]

        # Both players did to get "Ace" and have integer card
        if isinstance(current_card.number, int):
            return self.shape_dict_number[current_card.shape] * current_card.number

        # One player have royal card
        else:
            return self.shape_dict_royal_card[current_card.number]

    def find_round_winner(self):
        """
        :return: Rounds winner by game_rounds function.
        """
        print(START_GAME)
        game_round = 1
        for card1, card2 in zip(self.player1.cards, self.player2.cards):
            self.game_rounds(card1, card2, game_round)
            game_round += 1

    def find_game_winner(self):
        """
        :return: who won the most rounds and return him.
        """
        winner = None

        if self.player1.win_round_counter > self.player2.win_round_counter:
            winner = self.player1
        elif self.player2.win_round_counter > self.player1.win_round_counter:
            winner = self.player2

        self.print_winner(winner)

    def print_winner(self, winner):
        """
        :return: print the game winner.
        """
        if winner:
            print(WINNER_MESSAGE.format(winner_name=winner.name, round_counter=winner.win_round_counter))
        else:
            print(TIE)


if __name__ == '__main__':
    Game = Game()
    Game.start()
