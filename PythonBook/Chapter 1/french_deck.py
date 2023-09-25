from collections import namedtuple
from random import choice


#Card = namedtuple("Card", ["rank", "suit"])
class Card:
    def __init__(self, rank,suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return str(self.rank) + " " + self.suit

    def __repr__(self):
        return str(self)


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


beer_card = Card(7, "diamonds")
print(beer_card)


deck = FrenchDeck()
print(len(deck))
print(deck[-1])
print(deck[12::13])

print(Card(7, "diamonds") in deck)

for card in sorted(deck, key=spades_high):
    print(card)
