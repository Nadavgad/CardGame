from CardGame.constants import MIN, FIRST_MIDDLE, SECOND_MIDDLE, MAX


class Card:

    shape_dict_number = {"♥": 1, "♠": 2, "♦": 3, "♣": 4}
    shape_dict_royal_card = {"Prince": MIN, "Queen": FIRST_MIDDLE, "King": SECOND_MIDDLE}

    def __init__(self, number, shape):
        self.number = number
        self.shape = shape

    def calculate(self, card):

        """
        :param card: Card get number(2-10, Prince, Queen, King, Ace) and shape, Depending on the shape of the card the value of
        the card is calculated

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
        if self.number == "Ace" and card.number in ["Prince", "Queen", "King", "Ace"]:
            return MAX
        elif self.number == "Ace":
            return self.shape_dict_number[self.shape]

        # Both players did to get "Ace" and have integer card
        if isinstance(self.number, int):
            return self.shape_dict_number[self.shape] * self.number

        # One player have royal card
        else:
            return self.shape_dict_royal_card[self.number]

    def __str__(self):

        """
        when we share the cards each card is printed with its value
        :return: string of card number and card shape
        """
        return f"{self.number} of {self.shape}"
