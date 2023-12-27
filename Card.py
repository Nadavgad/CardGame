"""
class Summary :

Card get number(2-10, prince, queen, king, ace) and shape,
Depending on the shape of the card the value of the card is calculated:

if number type of integer :
Heart - card number multiply by 1.
Clover - card number multiply by 2.
Diamond - card number multiply by 3.
Leaf - card number is multiplied by 4.

if number type of Royal cards :

ace > king > queen > prince > Any number card

"""


class Card:
    def __init__(self, number, shape):
        self.number = number
        self.shape = shape

    def calculate(self, card):
        """
        :param card: Depending on the shape of the card the value of the card is calculated.
        :return: card value.
        """
        if type(self.number) is int:
            if self.shape == "Heart":
                return self.number * 1
            elif self.shape == "Clover":
                return self.number * 2
            elif self.shape == "Diamond":
                return self.number * 3
            elif self.shape == "Leaf":
                return self.number * 4
        else:
            if self.number == "prince":
                return 1000
            elif self.number == "queen":
                return 2000
            elif self.number == "king":
                return 3000
            elif self.number == "ace":
                if card.number in ["prince", "queen", "king", "ace"]:
                    return 4000
                else:
                    if self.shape == "Heart":
                        return 1
                    elif self.shape == "Clover":
                        return 2
                    elif self.shape == "Diamond":
                        return 3
                    else:
                        return 4

    """
    when we share the cards each card is printed with its value
    """
    def __str__(self):
        """
        :return: string of card number and card shape
        """
        return f"{self.number} of {self.shape}"
