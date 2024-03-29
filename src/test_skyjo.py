
""" TODO  """
from cards.card import Card
from cards.card_value_enum import CardValueEnum
from cards.card_status_enum import CardStatusEnum
from cards.player_board import PlayerBoard
from cards.discard import Discard

discard = Discard()
discard.append(Card(CardValueEnum.ONE))

test_skyjo = PlayerBoard()

test_skyjo._board = [
    [Card(CardValueEnum.FOUR, CardStatusEnum.HIDDEN), Card(CardValueEnum.FIVE,
                                                           CardStatusEnum.VISIBLE), Card(CardValueEnum.FIVE, CardStatusEnum.HIDDEN)],
    [None, None, None],
    [Card(CardValueEnum.FOUR, CardStatusEnum.VISIBLE), Card(CardValueEnum.FOUR,
                                                            CardStatusEnum.VISIBLE), Card(CardValueEnum.FOUR, CardStatusEnum.VISIBLE)],
    [None, None, None]
]

print(test_skyjo)
print('discard', discard)
print('test_skyjo.sum()', test_skyjo.sum())
print('test_skyjo.finish_playing()', test_skyjo.finish())
print('test_skyjo.skyjo(discard)', test_skyjo.skyjo(discard))
print('discard', discard)
print(test_skyjo)
print('test_skyjo.swap', test_skyjo.swap(
    Card(CardValueEnum.FIVE, CardStatusEnum.VISIBLE), 0, 0))
print(test_skyjo)
print('test_skyjo.skyjo(discard)', test_skyjo.skyjo(discard))
print('discard', discard)
print('test_skyjo.sum()', test_skyjo.sum())
print('test_skyjo.finish_playing()', test_skyjo.finish())
test_skyjo.reveal(0, 2)
print(test_skyjo)
print('test_skyjo.sum()', test_skyjo.sum())
print('test_skyjo.skyjo(discard)', test_skyjo.skyjo(discard))
print('test_skyjo.finish_playing()', test_skyjo.finish())
print('test_skyjo.sum()', test_skyjo.sum())
print(test_skyjo)
