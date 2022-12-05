import random
from game.piece import Piece


class Board:
    """handles actions related to setting up and receiving info from game board
    """
    def __init__(self, diff):
        """sets up board

        Args:
            diff: game difficulty
        """
        if diff == "easy":
            self._size = (10, 10)
            self._bombs = 10
        elif diff == "medium":
            self._size = (18, 18)
            self._bombs = 47
        elif diff == "hard":
            self._size = (24, 24)
            self._bombs = 100
        elif diff == "test":
            self._size = (10, 10)
            self._bombs = 0
        self._lost = False
        self._won = False
        self._num_clicked = 0
        self._num_non_bombs = 0
        self.set_init_board()

    def set_init_board(self):
        """sets up inital board where clicking on a bomb is impossible
        """
        self._board = []
        for row in range(self._size[0]):
            row = []
            for col in range(self._size[1]):
                has_bomb = False
                self._num_non_bombs += 1
                piece = Piece(has_bomb)
                row.append(piece)
            self._board.append(row)

    def set_board(self):
        """sets up board with bombs after first click is made
        """
        self._num_non_bombs = 0
        self._board = []
        for row in range(self._size[0]):
            x = row
            row = []
            for col in range(self._size[1]):
                if (x + 1, col + 1) in self._bomb_coordinates:
                    has_bomb = True
                else:
                    has_bomb = False
                    self._num_non_bombs += 1
                piece = Piece(has_bomb)
                row.append(piece)
            self._board.append(row)
        self._set_neighbors_board()

    def set_bombs(self, startbox):
        """sets coordinates of bombs on board

        Args:
            startbox: contains the coordinates of initial click location, where bombs cannot be placed
        """
        self._bomb_coordinates = []
        to_be_placed = self._bombs
        while True:
            if to_be_placed == 0:
                break
            for bomb in range(1, self._bombs + 1):
                if to_be_placed == 0:
                    break
                x = random.randint(1, self._size[0])
                y = random.randint(1, self._size[1])
                if (x, y) not in self._bomb_coordinates:
                    if (x, y) != (startbox[0] + 1, startbox[1] + 1):
                        self._bomb_coordinates.append((x, y))
                        to_be_placed -= 1
                        continue
                continue
        self.set_board()

    def _set_neighbors_board(self):
        """sets info of non-bomb squares on game board
        """
        for row in range(self._size[0]):
            for col in range(self._size[1]):
                piece = self._get_piece((row, col))
                neighbors = self._get_list_of_neighbors((row, col))
                piece.set_neighbors_piece(neighbors)

    def get_size(self):
        """gets size of game area

        Returns:
            tuple, game size
        """
        return self._size

    def _get_piece(self, index):
        """gets info regarding what tile of coordinates contain

        Args:
            index: board coordinates

        Returns:
            Bool, bomb info
        """
        return self._board[index[0]][index[1]]

    def _get_list_of_neighbors(self, index):
        """gets info of neighboring tiles per tile

        Args:
            index: tile coordinates

        Returns:
            list: info of neighboring tiles
        """
        neighbors = []
        for row in range(index[0] - 1, index[0] + 2):
            for col in range(index[1] - 1, index[1] + 2):
                out_of_bounds = row < 0 or row >= self._size[0] or col < 0 or col >= self._size[1]
                same = row == index[0] and col == index[1]
                if same or out_of_bounds:
                    continue
                neighbors.append(self._get_piece((row, col)))
        return neighbors

    def handle_click_board(self, piece, flag):
        """handles the click information given in game, and changes tile board and/or tile data accordingly

        Args:
            piece: tile info
            flag: if true, toggle flag, if false, ignore
        """
        if piece.get_clicked() or not flag and piece.get_flagged():
            return
        if flag:
            piece.toggle_flag()
            return
        piece.click()
        if piece.get_has_bomb():
            self._lost = True
            return
        self._num_clicked += 1
        if piece.get_num_around() != 0:
            return
        for neighbor in piece.get_neighbors():
            if not neighbor.get_has_bomb() and not neighbor.get_clicked():
                self.handle_click_board(neighbor, False)

    def get_lost(self):
        """gets status of lose state

        Returns:
            Bool, lost or not lost
        """
        return self._lost

    def get_won(self):
        """gets status of win state

        Returns:
            Bool, true if all non-bomb tiles are clicked
        """
        return self._num_non_bombs == self._num_clicked
