from card import Card
from card_status_enum import CardStatusEnum


class Discard:

    _discard: list[Card] = []

    def __init__(self):
        self._discard = []

    def append(self, card: Card):
        card.status = CardStatusEnum.VISIBLE
        self._discard.append(card)

    def draw(self) -> Card:
        return self._discard.pop()

    def clear(self):
        self._discard = []

    def last(self) -> Card:
        return self._discard[-1]

    def __str__(self):
        return str(self.last())
