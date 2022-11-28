class Piece():
    def __init__(self, HasBomb):
        self._HasBomb = HasBomb
        self._clicked = False
        self._flagged = False

    def GetHasBomb(self):
        return self._HasBomb

    def GetClicked(self):
        return self._clicked

    def GetFlagged(self):
        return self._flagged

    def SetNeighbors_piece(self, neighbors):
        self._neighbors = neighbors
        self.SetNumAround()

    def SetNumAround(self):
        self._NumAround = 0
        for piece in self._neighbors:
            if piece.GetHasBomb():
                self._NumAround += 1

    def GetNumAround(self):
        return self._NumAround

    def ToggleFlag(self):
        self._flagged = not self._flagged

    def click(self):
        self._clicked = True

    def GetNeighbors(self):
        return self._neighbors
