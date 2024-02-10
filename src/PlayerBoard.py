from Card import Card
from CardStatusEnum import CardStatusEnum
from Discard import Discard

class PlayerBoard:

    _board = []

    def __init__(self):
        self.clear()

    def clear(self):
        self._board = [[None for _ in range(3)] for _ in range(4)]

    def __str__(self):

        def card_to_str(card):
            if card is None:
                return "[------]"
            else:
                return str(card)


        dis = "" 
        for i in range(3):
            dis += " | ".join([card_to_str(self._board[j][i]) for j in range(4)]) + "\n"

        return dis
    
    def append(self, card: Card) -> bool:
        for j in range(4):
            for i in range(3):
                if self._board[j][i] is None:
                    self._board[j][i] = card
                    return True
        return False
    
    def sum(self):
        sum = 0 
        for j in range(4):
            for i in range(3):
                if self._board[j][i] is not None:
                    if self._board[j][i].status == CardStatusEnum.VISIBLE:
                        sum += self._board[j][i].value
        return sum

    def reveal(self, x, y):
        if self._board[x][y] is not None:
            if self._board[x][y].status == CardStatusEnum.HIDDEN:
                self._board[x][y].status = CardStatusEnum.VISIBLE
                return False
        return True
    
    def swap(self, card: Card, x, y) -> (bool, Card):
        if self._board[x][y] is None:
            return (False, card)
        
        self._board[x][y], card = card, self._board[x][y]
        return (True, card)
        

    def skyjo(self, discard: Discard) -> bool:

        def check_skyjo(cards: list[Card | None]) -> bool:
            for card in cards:
                if card is None:
                    return False
                if card.status == CardStatusEnum.HIDDEN:
                    return False
            return cards[0].value == cards[1].value == cards[2].value

        return_skyjo = False

        for x in range(4):
            if check_skyjo(self._board[x]):
                for y in range(3):
                    discard.append(self._board[x][y])
                    self._board[x][y] = None
                    return_skyjo = True

        return return_skyjo
    
    def finish_playing(self) -> bool:
        for x in range(4):
            for y in range(3):
                if self._board[x][y] is not None:
                    if self._board[x][y].status == CardStatusEnum.HIDDEN:
                        return False
        return True

