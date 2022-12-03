class Piece():
    def __init__(self, has_bomb):
        self._has_bomb = has_bomb
        self._clicked = False
        self._flagged = False
        self._neighbors = None
        self._num_around = None

    def get_has_bomb(self):
        return self._has_bomb

    def get_clicked(self):
        return self._clicked

    def get_flagged(self):
        return self._flagged

    def set_neighbors_piece(self, neighbors):
        self._neighbors = neighbors
        self.set_num_around()

    def set_num_around(self):
        self._num_around = 0
        for piece in self._neighbors:
            if piece.get_has_bomb():
                self._num_around += 1

    def get_num_around(self):
        return self._num_around

    def toggle_flag(self):
        self._flagged = not self._flagged

    def click(self):
        self._clicked = True

    def get_neighbors(self):
        return self._neighbors
