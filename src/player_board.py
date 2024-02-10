"""Module providing class PlayerBoard."""

from ast import Tuple
from card import Card
from card_status_enum import CardStatusEnum
from discard import Discard


class PlayerBoard:
    """
    Represents the player's board in the Skyjo game.

    The player board is a 4x3 grid where cards can be placed. It provides methods for managing the cards on the board,
    such as appending cards, revealing cards, swapping cards, checking for Skyjo combinations, and checking if the board
    is finished.

    Attributes:
        _board (list[list[Card | None]]): The 4x3 grid representing the player board.

    Methods:
        __init__: Initializes the player board by calling the clear method.
        clear: Clears the player board by setting all positions to None.
        __str__: Returns a string representation of the player board.
        append: Appends a card to the player board.
        sum: Calculates the sum of the visible cards on the player board.
        reveal: Reveals a card at the specified position on the board.
        swap: Swaps a card with the card at the specified position on the board.
        skyjo: Checks if there is a valid Skyjo combination on the player's board.
        finish: Checks if the player board is finished.
    """
    _board = []

    def __init__(self):
        self.clear()

    def clear(self):
        """Clear the player board by setting all positions to None."""
        self._board = [[None for _ in range(3)] for _ in range(4)]

    def __str__(self):

        def card_to_str(card):
            if card is None:
                return "[------]"
            return str(card)

        return_str = ""
        for i in range(3):
            return_str += " | ".join([card_to_str(self._board[j][i])
                                      for j in range(4)]) + "\n"

        return return_str

    def append(self, card: Card) -> bool:
        """Append a card to the player board."""
        for j in range(4):
            for i in range(3):
                if self._board[j][i] is None:
                    self._board[j][i] = card
                    return True
        return False

    def sum(self):
        """Function calculate tue sum of the visible card."""

        calculate_sum = 0
        for j in range(4):
            for i in range(3):
                if self._board[j][i] is not None:
                    if self._board[j][i].status == CardStatusEnum.VISIBLE:
                        calculate_sum += self._board[j][i].value
        return calculate_sum

    def reveal(self, x, y):
        """
        Reveals a card at the specified position on the board.

        Args:
            x (int): The x-coordinate of the card.
            y (int): The y-coordinate of the card.

        Returns:
            bool: True if the card is already revealed or does not exist, False otherwise.
        """
        if self._board[x][y] is not None:
            if self._board[x][y].status == CardStatusEnum.HIDDEN:
                self._board[x][y].status = CardStatusEnum.VISIBLE
                return False
        return True

    def swap(self, card: Card, x: int, y: int) -> Tuple[bool, Card]:
        """
        Swaps the given card with the card at the specified position on the board.

        Args:
            card (Card): The card to be swapped.
            x (int): The x-coordinate of the position.
            y (int): The y-coordinate of the position.

        Returns:
            Tuple[bool, Card]: A tuple containing a boolean value indicating whether the swap was successful
            and the card that was previously at the specified position.
        """
        if self._board[x][y] is None:
            return (False, card)

        self._board[x][y], card = card, self._board[x][y]
        return (True, card)

    def skyjo(self, discard: Discard) -> bool:
        """
        Checks if there is a valid Skyjo combination on the player's board and updates the discard pile accordingly.

        Args:
            discard (Discard): The discard pile to append the cards to.

        Returns:
            bool: True if a Skyjo combination was found and cards were appended to the discard pile, False otherwise.
        """

        def check_skyjo(cards: list[Card | None]) -> bool:
            """
            Checks if a list of cards forms a valid Skyjo combination.

            Args:
                cards (list[Card | None]): The list of cards to check.

            Returns:
                bool: True if the cards form a valid Skyjo combination, False otherwise.
            """
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

    def finish(self) -> bool:
        """
        Checks if the player board is finished.

        Returns:
            bool: True if the player board is finished, False otherwise.
        """
        for x in range(4):
            for y in range(3):
                if self._board[x][y] is not None:
                    if self._board[x][y].status == CardStatusEnum.HIDDEN:
                        return False
        return True
