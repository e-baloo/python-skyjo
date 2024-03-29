"""Module providing class Card."""

from cards.card_value_enum import CardValueEnum
from cards.card_status_enum import CardStatusEnum


class Card:
    """
    Class representing a card.
    """

    _value: CardValueEnum = None
    _status: CardStatusEnum = CardStatusEnum.HIDDEN

    def __init__(self, value: CardValueEnum, status: CardStatusEnum = CardStatusEnum.HIDDEN):
        self._value = value
        self._status = status

    def __eq__(self, other):
        if isinstance(other, Card):
            return self._value == other._value
        return False

    def __str__(self):
        if self._status == CardStatusEnum.VISIBLE:
            return f"{self._value.value:^6d}"
        return f"({self._value.value:^4d})"

    @property
    def value(self) -> int:
        """The value of the card."""
        return self._value.value

    @property
    def status(self) -> CardStatusEnum:
        """The status of the card."""
        return self._status

    @status.setter
    def status(self, status: CardStatusEnum):
        self._status = status

    def reveal(self):
        """Reveals the card."""
        self._status = CardStatusEnum.VISIBLE
