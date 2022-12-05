class Piece():
    """contains game piece / asset info
    """
    def __init__(self, has_bomb):
        """sets up class

        Args:
            has_bomb: info on whether piece contains bomb
        """
        self._has_bomb = has_bomb
        self._clicked = False
        self._flagged = False
        self._neighbors = None
        self._num_around = None

    def get_has_bomb(self):
        """

        Returns:
            bool: returns info on whether piece contains bomb
        """
        return self._has_bomb

    def get_clicked(self):
        """

        Returns:
            bool: info on whether tile was clicked
        """
        return self._clicked

    def get_flagged(self):
        """

        Returns:
            bool: info on whther tile is flagged
        """
        return self._flagged

    def set_neighbors_piece(self, neighbors):
        """sets up setting number of bombs around piece

        Args:
            neighbors: pieces around given piece
        """
        self._neighbors = neighbors
        self.set_num_around()

    def set_num_around(self):
        """sets the number on the given tile / amount of bombs around given tile
        """
        self._num_around = 0
        for piece in self._neighbors:
            if piece.get_has_bomb():
                self._num_around += 1

    def get_num_around(self):
        """

        Returns:
           int, number of bombs around given tile
        """
        return self._num_around

    def toggle_flag(self):
        """puts flag on tile
        """
        self._flagged = not self._flagged

    def click(self):
        """checks if click took place
        """
        self._clicked = True

    def get_neighbors(self):
        """

        Returns:
            list, tiles around given piece
        """
        return self._neighbors
