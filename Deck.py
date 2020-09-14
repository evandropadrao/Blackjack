import random
import main
import Card


class Deck:

    def __init__(self):
        self.__deck = []

        for suit in main.suits:
            for rank in main.ranking:
                self.__deck.append(Card.Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.__deck)

    def deal(self):
        single_card = self.__deck.pop()
        return single_card

    def __str__(self):
        deck_comp = ""
        for card in self.__deck:
            deck_comp += ' ' + card.__str__()

        return "Deck has: " + deck_comp
