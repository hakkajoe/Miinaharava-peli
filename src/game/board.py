import random
from game.piece import Piece


class Board:
    def __init__(self, diff):
        if diff == "easy":
            self._size = (10, 10)
            self._bombs = 10
        elif diff == "medium":
            self._size = (18, 18)
            self._bombs = 47
        elif diff == "hard":
            self._size = (24, 24)
            self._bombs = 100
        self._lost = False
        self._won = False
        self._num_clicked = 0
        self._num_non_bombs = 0
        self.set_init_board()

    def set_init_board(self):
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
        for row in range(self._size[0]):
            for col in range(self._size[1]):
                piece = self._get_piece((row, col))
                neighbors = self._get_list_of_neighbors((row, col))
                piece.set_neighbors_piece(neighbors)

    def get_size(self):
        return self._size

    def _get_piece(self, index):
        return self._board[index[0]][index[1]]

    def _get_list_of_neighbors(self, index):
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
        return self._lost

    def get_won(self):
        return self._num_non_bombs == self._num_clicked
