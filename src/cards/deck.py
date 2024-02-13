"""Module providing class Deck."""

from random import shuffle
from cards.card import Card
from cards.card_value_enum import CardValueEnum
from cards.card_status_enum import CardStatusEnum

DISTRIBUTION = [
    [5, [CardValueEnum.NEGATIVE_TOW]],
    [15, [CardValueEnum.ZERO]],
    [10, [CardValueEnum.NEGATIVE_ONE, CardValueEnum.ONE, CardValueEnum.TWO, CardValueEnum.THREE,
          CardValueEnum.FOUR, CardValueEnum.FIVE, CardValueEnum.SIX, CardValueEnum.SEVEN,
          CardValueEnum.EIGHT, CardValueEnum.NINE, CardValueEnum.TEN, CardValueEnum.ELEVEN,
          CardValueEnum.TWELVE]],
]


class Deck:
    """
    Class representing a deck of cards.
    """

    _deck: list[Card] = []

    def __init__(self):
        self.clear()

    def shuffle(self):
        """Shuffle the deck."""
        shuffle(self._deck)
        for card in self._deck:
            card.status = CardStatusEnum.HIDDEN

    def draw(self) -> Card:
        """Draw a card from the deck."""
        return self._deck.pop()

    def __str__(self):
        return str(self._deck[-1])

    def __len__(self):
        return len(self._deck)

    def append(self, card: Card):
        """Append a card to the deck."""
        self._deck.append(card)

    def clear(self):
        """Clear the deck."""
        self._deck = []
        for (count, values) in DISTRIBUTION:
            for _ in range(count):
                for value in values:
                    self._deck.append(
                        Card(value=value, status=CardStatusEnum.HIDDEN))

    def count(self):
        """Return the number of cards in the deck."""
        return len(self._deck)

    def get(self) -> Card:
        """Return the last card in the deck."""
        return self._deck[-1]
