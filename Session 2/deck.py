"""
Module defining a standard 52-card deck and individual card representation.

Includes:
- Card: representing a single playing card with rank and suit.
- Deck: representing a full deck of 52 unique cards with shuffling and dealing logic.

Demonstrates deck creation, shuffling, and dealing.
"""

import random


class Card:
    """
    Class representing a single playing card.

    Attributes:
        RANKS (list): Valid card ranks from 2 to Ace.
        SUITS (list): Valid suits: spades, clubs, diamonds, hearts.
    """

    RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    SUITS = ["♠", "♣", "♦", "♥"]

    def __init__(self, rank, suit):
        """
        Initialize a Card instance with a valid rank and suit.

        Args:
            rank (int or str): The rank of the card (2–10, J, Q, K, A).
            suit (str): The suit of the card (♠, ♣, ♦, ♥).

        Raises:
            ValueError: If rank or suit is invalid.
        """
        if rank not in self.RANKS:
            raise ValueError(f"Invalid rank: {rank}")
        if suit not in self.SUITS:
            raise ValueError(f"Invalid suit: {suit}")
        self._rank = rank
        self._suit = suit

    def __str__(self):
        """
        Return a string representation of the card.

        Returns:
            str: Card rank followed by suit, e.g., 'A♠'
        """
        return f"{self.rank}{self.suit}"

    def __repr__(self):
        """
        Return a developer-friendly string representation of the card.

        Returns:
            str: Same as __str__.
        """
        return self.__str__()

    @property
    def rank(self):
        """
        Card rank accessor.

        Returns:
            int or str: The rank of the card.
        """
        return self._rank

    @property
    def suit(self):
        """
        Card suit accessor.

        Returns:
            str: The suit of the card.
        """
        return self._suit


class Deck:
    """
    Class representing a standard deck of 52 playing cards.

    Methods:
        shuffle(): Randomizes the order of cards in the deck.
        deal(): Removes and returns the top card from the deck.
    """

    def __init__(self):
        """
        Initialize a new deck containing 52 cards.
        """
        _cards = []
        for rank in Card.RANKS:
            for suit in Card.SUITS:
                _cards.append(Card(rank, suit))
        self._deck = _cards

    @property
    def deck(self):
        """
        Access the list of cards in the deck.

        Returns:
            list of Card: The cards remaining in the deck.
        """
        return self._deck

    def __str__(self):
        """
        Return a string representation of the deck.

        Returns:
            str: Stringified list of cards in the deck.
        """
        return f"{self._deck}"

    def shuffle(self):
        """
        Shuffle the deck in place using random.shuffle.
        """
        random.shuffle(self._deck)

    def deal(self):
        """
        Deal the top card from the deck.

        Returns:
            Card: The card removed from the top of the deck.
        """
        return self._deck.pop(0)


if __name__ == "__main__":
    """
    Demonstrates deck functionality:
    - Create a deck
    - Shuffle it
    - Deal the top card
    """
    deck = Deck()
    print(deck)
    deck.shuffle()
    print(deck.deal())

    # c1 = Card("A", "♠")
    # print(c1)