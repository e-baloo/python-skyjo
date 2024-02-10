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
discard.append(deck.draw())

player_boards = [PlayerBoard() for _ in range(3)]

for _ in range(12):
    for player_board in player_boards:
        player_board.append(deck.draw())

for player_board in player_boards:

    while (player_board.reveal(random.randint(0, 3), random.randint(0, 2))) :
        pass
    while (player_board.reveal(random.randint(0, 3), random.randint(0, 2))) :
        pass

    print(player_board)
    print('sum', player_board.sum())
    print('----------------------------')

print('deck   ', deck)
print('discard', discard)






"""
Transitions :

    Player (Hand (one card) / Board (12 cards))
    - if deck is empty (Step 0)
        - draw saved card from discard
        - move discard cards from deck
        - shuffle deck
        - append saved card from discard
    
    - draw card from deck or discard (Choice 1)
        - (deck) append card to hand from deck
        - (discard) append card to hand from discard
        - reveal card in hand (Step 2)

    - swap card in hand with board or discard (Choice 3)
        - (discard) 
            - append hand card to discard
            - hand card is None
            - reveal card from board
        - (swap) 
            - hand card with board
            - append hand card to discard -> hand card is None

    - check skyjo
        - append board cards to discard
        - remove board cards
    
    - finish playing ?
    

"""
