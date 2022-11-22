from game.piece import Piece
from random import random

class Board:
    def __init__(self, size, prob):
        self._size = size
        self._prob = prob
        self.SetBoard()

    def SetBoard(self):
        self._board = []
        for row in range(self._size[0]):
            row = []
            for col in range(self._size[1]):
                HasBomb = random() < self._prob
                piece = Piece(HasBomb)
                row.append(piece)
            self._board.append(row)

    def GetSize(self):
        return self._size

    def GetPiece(self, index):
        return self._board[index[0]][index[1]]