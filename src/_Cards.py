from Card import Card
from typing import List


class Cards :
    _cards: List[Card] = []

    def __init__(self, cards: List[Card] | None = None):

        if cards is not None:
            self._cards = cards
        else:
            self._cards = []

    def add(self, card: Card):
        self._cards.append(card)

    def get(self, index: int) -> Card:
        return self._cards[index]

    def count(self) -> int:
        return len(self._cards)

    def remove(self, card: Card):
        self._cards.remove(card)

    def sum(self) -> int:
        return sum([card.value() for card in self._cards])    
