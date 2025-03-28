"""
Module that defines a `Hand` class to simulate a poker hand drawn from a shuffled deck.

Features:
- Drawing 5 cards
- String representation of the hand
- Evaluating poker hand types: flush, pair, two pair, three-of-a-kind, full house, four-of-a-kind, straight

Includes a simulation to estimate the probability of drawing a straight.
"""

from deck import Deck, Card


class Hand:
    """
    Represents a poker hand containing 5 cards drawn from a deck.

    Provides properties to determine the hand type (flush, pair, etc.).
    """

    def __init__(self):
        """
        Initialize the Hand by drawing 5 cards from a deck.
        """
        hand = []
        for i in range(5):
            hand.append(deck.deal())
        self._hand = hand

    @property
    def hand(self):
        """
        Accessor for the hand of cards.

        Returns:
            list: List of 5 Card objects in the hand.
        """
        return self._hand

    def __str__(self):
        """
        String representation of the hand.

        Returns:
            str: List-style string showing the 5 cards in hand.
        """
        return str(self.hand)

    @property
    def is_flush(self):
        """
        Determine if the hand is a flush (all cards share the same suit).

        Returns:
            bool: True if all cards have the same suit, False otherwise.
        """
        for card in self.hand:
            if card.suit != self.hand[0].suit:
                return False
        return True

    @property
    def num_matches(self):
        """
        Calculate total number of matching rank comparisons in the hand.

        Returns:
            int: Total number of matching card rank pairs.
        """
        matches = 0
        for i in range(5):
            for j in range(5):
                if i == j:
                    continue
                elif self.hand[i].rank == self.hand[j].rank:
                    matches += 1
        return matches

    @property
    def is_pair(self):
        """
        Determine if the hand is a single pair.

        Returns:
            bool: True if hand has one pair, False otherwise.
        """
        return self.num_matches == 2

    @property
    def is_2pair(self):
        """
        Determine if the hand has two pairs.

        Returns:
            bool: True if hand has two distinct pairs, False otherwise.
        """
        return self.num_matches == 4

    @property
    def is_trip(self):
        """
        Determine if the hand is three-of-a-kind.

        Returns:
            bool: True if hand has three cards of the same rank, False otherwise.
        """
        return self.num_matches == 6

    @property
    def is_full(self):
        """
        Determine if the hand is a full house (3 of a kind + a pair).

        Returns:
            bool: True if hand is a full house, False otherwise.
        """
        return self.num_matches == 8

    @property
    def is_quad(self):
        """
        Determine if the hand is four-of-a-kind.

        Returns:
            bool: True if hand has four cards of the same rank, False otherwise.
        """
        return self.num_matches == 12

    @property
    def is_straight(self):
        """
        Determine if the hand is a straight (5 consecutive ranks).

        Returns:
            bool: True if hand is a straight, False otherwise.
        """
        if self.num_matches != 0:
            return False
        self.hand.sort(key=lambda card: Card.RANKS.index(card.rank))
        return Card.RANKS.index(self.hand[-1].rank) == Card.RANKS.index(self.hand[0].rank) + 4


# Simulation to estimate probability of drawing a straight in a random 5-card hand

count = 0
matches = 0

while matches < 1000:
    deck = Deck()
    deck.shuffle()
    h = Hand()
    count += 1
    if h.is_straight:
        matches += 1

print(100 * (matches / count))  # Estimated straight percentage