from CardGame.constants import MIN, FIRST_MIDDLE, SECOND_MIDDLE, MAX, CARD_REPRESENTATION


class Card:

    def __init__(self, number, shape):
        self.number = number
        self.shape = shape

    def __str__(self):

        """
        when we share the cards each card is printed with its value
        :return: string of card number and card shape
        """
        return CARD_REPRESENTATION.format(card_number=self.number, card_shape=self.shape)
