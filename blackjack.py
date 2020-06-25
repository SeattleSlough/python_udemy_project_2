import random

suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven",
         "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7,
          "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}

playing = True


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return "%s of %s" % (self.rank, self.suit)


class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        for card in self.deck:
            return str(card)

    def __len__(self):
        return len(self.deck)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):

        count = 0

        while count <= 3:
            card = self.deck.pop(count)
            if card.rank == "Ace":
                player.aces += 1
            player.add_card(card)
            count += 1

            card = self.deck.pop(count)
            if card.rank == "Ace":
                dealer.aces += 1
            dealer.add_card(card)
            count += 1


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        if card.rank == "Ace":
            self.aces += 1

        self.cards.append(card)

    def show_hand(self):
        for card in self.cards:
            print(card)

    def adjust_for_aces(self):
        self.value -= 10


player = Hand()
dealer = Hand()

hoyle = Deck()
hoyle.shuffle()

hoyle.deal()

player.show_hand()

player.add_card(hoyle.deck.pop(0))
