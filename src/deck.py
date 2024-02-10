"""Module providing class Deck."""

from card import Card
from card_value_enum import CardValueEnum
from card_status_enum import CardStatusEnum

DISTRIBUTION = [
    [5, [CardValueEnum.NEGATIVE_TOW]],
    [15, [CardValueEnum.ZERO]],
    [10, [CardValueEnum.NEGATIVE_ONE, CardValueEnum.ONE, CardValueEnum.TWO, CardValueEnum.THREE, CardValueEnum.FOUR, CardValueEnum.FIVE,
          CardValueEnum.SIX, CardValueEnum.SEVEN, CardValueEnum.EIGHT, CardValueEnum.NINE, CardValueEnum.TEN, CardValueEnum.ELEVEN, CardValueEnum.TWELVE]],
]


class Deck:
    """
    Class representing a deck of cards.
    """

    _deck: list[Card] = []

    def __init__(self):
        self.clear()

    def shuffle(self):
        from random import shuffle
        shuffle(self._deck)
        for card in self._deck:
            card.status = CardStatusEnum.HIDDEN

    def draw(self) -> Card:
        return self._deck.pop()

    def __str__(self):
        return str(self._deck[-1])

    def __len__(self):
        return len(self._deck)

    def append(self, card: Card):
        self._deck.append(card)

    def clear(self):
        self._deck = []
        for (count, values) in DISTRIBUTION:
            for _ in range(count):
                for value in values:
                    self._deck.append(
                        Card(value=value, status=CardStatusEnum.HIDDEN))

    def count(self):
        return len(self._deck)
