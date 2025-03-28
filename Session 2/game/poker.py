"""
Module that defines a Hand class to model a poker hand of 5 cards dealt from a deck.

Includes functionality to:
- Deal a 5-card hand
- Represent the hand as a string
- Check if the hand is a flush (all cards of the same suit)

Demonstrates drawing hands repeatedly until a flush is found.
"""

from deck import Deck, Card


class Hand:
    """
    Class representing a 5-card poker hand.

    Attributes:
        _hand (list of Card): A list of 5 Card instances dealt from a deck.
    """

    def __init__(self):
        """
        Initialize the Hand by dealing 5 cards from a freshly created Deck.
        """
        hand = []
        for i in range(5):
            hand.append(deck.deal())
        self._hand = hand

    @property
    def hand(self):
        """
        Property to access the cards in the hand.

        Returns:
            list of Card: The list of Card objects in the hand.
        """
        return self._hand

    def __str__(self):
        """
        Return a string representation of the hand.

        Returns:
            str: Stringified list of Card objects.
        """
        return str(self.hand)

    @property
    def is_flush(self):
        """
        Check if all cards in the hand share the same suit.

        Returns:
            bool: True if all cards have the same suit, False otherwise.
        """
        for card in self.hand:
            if card.suit != self.hand[0].suit:
                return False
        return True


# Continuously deal and shuffle a new deck until a flush hand is found
while True:
    deck = Deck()
    deck.shuffle()
    h = Hand()
    if h.is_flush:
        print(h)
        break