import random

suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven",
         "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7,
          "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        pass


class Deck:

    def __init__(self):
        self.deck = []

    def __str__(self):
        pass

    def shuffle(self, suits, ranks):
        for suit in suits:
            for rank in ranks:
                pass

    def deal(self):
        pass


class Hand:
    def __init__(self):
        pass


playing = True