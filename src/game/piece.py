class Piece():
    def __init__(self, HasBomb):
        self._HasBomb = HasBomb
        self._clicked = False
        self._flagged = False

    def GetHasBomb(self):
        return self._HasBomb

    def Getclicked(self):
        return self._clicked

    def GetFlagged(self):
        return self._flagged

    def GetNumAround(self):
        return self._NumAround