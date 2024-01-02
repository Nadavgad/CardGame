from CardGame.Card import Card
import random

from CardGame.Player import Player
from CardGame.constants import MENU_CONTENT, START_GAME, FIRST_PLAYER, SECOND_PLAYER, TIE, PLAYER_CARDS, \
    SAME_CARD_NUMBER, SHAPES, NUMBERS


class Game:

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

    def game_rounds(self, card1, card2, game_round):
        """
        :param game_round: The game round, there is 24 rounds.
        :param card1: Calculate the value of the cards1
        :param card2: Calculate the value of the cards2
        :return: The round winner.
        """

        value1 = card1.calculate(card2)
        value2 = card2.calculate(card1)

        print(f"\nGAME ROUND {game_round} : {self.player1.name} has played {card1.number} of {card1.shape}, its "
              f"value is {value1}\n"
              f"{self.player2.name} has played {card2.number} of {card2.shape}, its value is {value2}")

        if value1 > value2:

            self.player1.win_round_counter += 1
            print(f"{self.player1.name}'s WIN ROUND {game_round}.\n")

        elif value1 < value2:

            self.player2.win_round_counter += 1
            print(f"{self.player2.name}'s WIN ROUND {game_round}.\n")

        else:
            print(TIE)

    def find_round_winner(self):
        """
        :return: Rounds winner by game_rounds function.
        """
        print(START_GAME)
        game_round = 1
        for card1, card2 in zip(self.player1.cards, self.player2.cards):
            self.game_rounds(card1, card2, game_round)
            game_round += 1

    @staticmethod
    def __print_cards(player):
        """
        :param player:  get player.
        :return: print each card from player cards
        """
        print(f"\n{player.name}'s cards : \n")
        for card in player.cards:
            print(card)

    def print_players_cards(self):
        """
        :return: Print player cards.
        """
        print(PLAYER_CARDS)
        self.__print_cards(self.player1)
        self.__print_cards(self.player2)

    def print_winner(self, winner):
        """
        :return: print the game winner.
        """
        if winner:
            print(
                f"\n **********   THE WINNER IS {winner.name} WHO WON IN {winner.win_round_counter} ROUNDS   ********** "
                f"\n \n \n")
        else:
            print(TIE)

    def find_game_winner(self):
        """
        :return: who won the most rounds and return him.
        """

        if self.player1.win_round_counter > self.player2.win_round_counter:
            winner = self.player1
        elif self.player2.win_round_counter > self.player1.win_round_counter:
            winner = self.player2

        self.print_winner(winner)

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


if __name__ == '__main__':
    Game = Game()
    Game.start()
