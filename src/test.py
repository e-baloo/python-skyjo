import random
from Card import Card
from CardValueEnum import CardValueEnum
from CardStatusEnum import CardStatusEnum
from Deck import Deck
from PlayerBoard import PlayerBoard
from Discard import Discard

deck = Deck()
discard = Discard()

deck.shuffle()
discard.append(deck.pop())

player_boards = [PlayerBoard() for _ in range(4)]

for _ in range(12):
    for player_board in player_boards:
        player_board.append(deck.pop())

print('discard', discard)
for player_board in player_boards:

    while (player_board.reveal(random.randint(0, 3), random.randint(0, 2))) :
        pass
    while (player_board.reveal(random.randint(0, 3), random.randint(0, 2))) :
        pass

    print(player_board)
    print('sum', player_board.sum())
    print('----------------------------')



