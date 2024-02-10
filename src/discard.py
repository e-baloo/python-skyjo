"""Module providing class Discard."""

from card import Card
from card_status_enum import CardStatusEnum


class Discard:
    """
    Class representing the discard pile.
    """

    _discard: list[Card] = []

    def __init__(self):
        self._discard = []

    def append(self, card: Card):
        """Append a card to the discard pile."""
        card.status = CardStatusEnum.VISIBLE
        self._discard.append(card)

    def draw(self) -> Card:
        """Draw a card from the discard pile."""
        return self._discard.pop()

    def clear(self):
        """Clear the discard pile."""
        self._discard = []

    def last(self) -> Card:
        """Return the last card in the discard pile."""
        return self._discard[-1]

    def __str__(self):
        return str(self.last())
