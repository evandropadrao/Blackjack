
class Card:

    def __init__(self, suit, rank):
        self.__suit = suit
        self.__rank = rank

    def __str__(self):
        return self.__rank + " of " + self.__suit

    def grab_suit(self):
        return self.__suit

    def grab_rank(self):
        return self.__rank

    def draw(self):
        print(" ", self.__rank, "of", self.__suit)

