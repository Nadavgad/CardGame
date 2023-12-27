from CardGame.Card import Card
import random

from CardGame.Player import Player

"""

Class Summary :

System manages the card game.

"""


class System:
    """
    System constructor - create cards_array by the function generate_cards.
    and create 2 players.
    """
    menu_content = """Welcome to the game of wonders!\n"""
    start_game = """ \n                  ***** GAME STARTED ***** """

    def __init__(self):
        self.cards_array = self.generate_cards()
        self.player1 = None
        self.player2 = None

    """
    Start function get 2 names from the console and put it on players names.
    then start distribute_cards function.
    and print players cards.
    and find the game winner.
    """

    def start(self):
        """
        :return: The game winner with his card counter
        """
        print(self.menu_content)
        player1_name = input("Please select the first player name\n")
        self.player1 = Player(player1_name)
        player2_name = input("Please select the second player name\n")
        self.player2 = Player(player2_name)

        self.distribute_cards()
        self.__print_cards(self.player1)
        self.__print_cards(self.player2)
        winner = self.find_winner()

        """ Print the winner's name and card counter """
        if winner:
            print(f"\n **********   THE WINNER IS {winner.name} WHO WON IN {winner.round_counter} ROUNDS   ********** "
                  f"\n \n \n")
        else:
            print("It's a tie!")

    @staticmethod
    def __print_cards(player):
        """
        :param player:  get player.
        :return: print each card from player cards
        """
        print(" Players cards \n")
        print(f"\n{player.name}'s cards : \n")
        for card in player.cards:
            print(card)

    """
    generate_cards - Function that have:
    numbers list of numbers 2 - 10 and Royal cards.
    shape list of cards shape.
    new cards list that create Card with number from numbers list and shape from shapes list.
    *Note - WHEN YOU CRATE CARD, CARD CLASS PRINT THE CARD THAT HAS CREATED. 
    """

    @staticmethod
    def generate_cards():
        """
        :return: cards list that include number and shape.
        """
        numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, "prince", "queen", "king", "ace"]
        shapes = ["Clover", "Heart", "Diamond", "Leaf"]
        cards = [Card(number, shape) for number in numbers for shape in shapes]

        return cards

    """
    distribute_cards - function that get player1 and player2 and share the cards from cards_array to each player list,
    random.shuffle - mix cards_array.
    half_size - get length cards_array/2.
    player1_cards - Creates a list containing the first half of the shuffled cards.
    player2_cards - Creates a list containing the second half of the shuffled cards.
    The two for loops distribute the cards to player1 and player2 by calling the add_card method on each player.
    display_cards - function that print all the cards in cards_array.
    """

    def distribute_cards(self):
        """
        :return: split the cards list to 2 lists. list for player 1 and list for player 2.
        """

        random.shuffle(self.cards_array)

        # Split the cards into two halves
        half_size = len(self.cards_array) // 2
        self.player1.cards = self.cards_array[:half_size]
        self.player2.cards = self.cards_array[half_size:]

    def display_cards(self):
        print("All Cards in the System:")
        for card in self.cards_array:
            print(card)

    def find_winner(self):
        """
        find_winner - find the winner for each round and the game winner.
        :return: The winner.
        """

        # Validate both players have same number of cards
        if len(self.player1.cards) != len(self.player2.cards):
            raise ValueError("Both players must have the same number of cards.")

        """
        Loop that creating tuples (card1, card2) in each iteration of the loop.
        for card1 and card2 we calculate the value of the cards.
        values will be in value1 and value2.
        
        if value1 > value2 payer1 counter++, else player2 counter++.
        
        In the end we check who won the most rounds and he will be the winner of the game and we return him.
        """
        print(self.start_game)
        counter = 0
        for card1, card2 in zip(self.player1.cards, self.player2.cards):
            value1 = card1.calculate(card2)
            value2 = card2.calculate(card1)

            counter += 1
            print(f"\nGAME ROUND {counter} : {self.player1.name} has played {card1.number} of {card1.shape}, its "
                  f"value is {value1}\n"
                  f"{self.player2.name} has played {card2.number} of {card2.shape}, its value is {value2}")
            if value1 > value2:

                self.player1.round_counter += 1
                print(f"{self.player1.name}'s WIN ROUND {counter}:\n")
            elif value1 < value2:

                self.player2.round_counter += 1
                print(f"{self.player2.name}'s WIN ROUND {counter}:\n")

        if self.player1.round_counter > self.player2.round_counter:
            return self.player1
        elif self.player2.round_counter > self.player1.round_counter:
            return self.player2

        # Return None in case of a tie
        return None


if __name__ == '__main__':
    system = System()
    system.start()
