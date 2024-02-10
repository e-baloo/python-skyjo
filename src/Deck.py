from Card import Card
from CardValueEnum import CardValueEnum
from CardStatusEnum import CardStatusEnum   

DISTRIBUTION = [
    [5, [CardValueEnum.NEGATIVE_TOW]],
    [15, [CardValueEnum.ZERO]],
    [10, [CardValueEnum.NEGATIVE_ONE, CardValueEnum.ONE, CardValueEnum.TWO, CardValueEnum.THREE, CardValueEnum.FOUR, CardValueEnum.FIVE, CardValueEnum.SIX, CardValueEnum.SEVEN, CardValueEnum.EIGHT, CardValueEnum.NINE, CardValueEnum.TEN, CardValueEnum.ELEVEN, CardValueEnum.TWELVE]],
]


class Deck:

    _deck: list[Card] = []

    def __init__(self):
        self.clear()

    def shuffle(self):
        from random import shuffle
        shuffle(self._deck)

    def pop(self) -> Card:
        return self._deck.pop()

    def __str__(self):
        return str([str(card) for card in self._deck])

    def __len__(self):
        return len(self._deck)

    def clear(self):
        self._deck = []
        for (count, values) in DISTRIBUTION:
                    for _ in range(count):
                        for value in values:
                            self._deck.append(Card(value=value, status=CardStatusEnum.HIDDEN))

    def count(self):
        return len(self._deck)
