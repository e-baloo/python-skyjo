from Card import Card
from CardStatusEnum import CardStatusEnum

class Discard:

    _discard: list[Card] = []

    def __init__(self):
        self._discard = []

    def append(self, card: Card):
        card.status = CardStatusEnum.VISIBLE
        self._discard.append(card)

    def pop(self) -> Card:
        return self._discard.pop()

    def last(self) -> Card:
        return self._discard[-1]
    
    def clear(self):
        self._discard = []

    def __str__(self):
        return str(self.last())

