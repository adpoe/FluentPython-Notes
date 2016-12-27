""" Code from Chapter 1 of Fluent Python
    Exploring the Python Data Model
"""

# A Pythonic Card deck
# Shows the power of implementing two special methods
# __getitem__ and __len__ (dunder methods)

import collections
from math import hypot

Card = collections.namedtuple('Card', ['rank', 'suit'])
# use namedtuple to build classes of objects that are just
# bundles of attributes, with no custom methods
# you can index each card object by these names

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    # allows a deck instance to respond to len() fn
    def __len__(self):
        return len(self._cards)

    # read specific cards from the deck like this:
    # deck[0] --> Card(rank='2', suit='spades)
    # works for indices 0 to 51
    def __getitem__(self, position):
        return self._cards[position]



# get a random card like this:
"""
    from random import choice
    choice(deck)
"""

# means users of our class don't have to memorize arbitrary method
# names for standard operations like getting a random value, or size.

# AND our deck automatically supports slicing, by delgating to the
# [] operator to self._cards

# and just by implemeting __getitem__ our deck is also iterable
# can use 'for card in deck:'
#               .....

# Notes:
# - if a collection has no __contains__ method, it does a sequential scan

# fn to allow sorting cards by rank
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(self,card):
    rank_value = FrenchDeck.ranks.index(card.rank) # get the index as an integer
    return rank_value * len(suit_values) + suit_values[card.suit]

"""
    Now we can do this:
    for card in sorted(deck, key=spades_high):
        print(card)
"""

# by implementing __len__ and __getitem__ the deck behaves like
# a standard Python sequence.


"""
    A Simple 2D Vector Class
"""

# lets us use + and * right on instances of the class, directly.
# the interpreter calls these special methods NOT us.
class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # gives us a string representation
    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    # vector evaluates to True when it is nonzero
    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
