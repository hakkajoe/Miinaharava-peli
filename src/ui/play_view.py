from tkinter import ttk, constants
from services.game_service import game_service
from game.game import Game
from game.board import Board


class PlayView:
    def __init__(self, root, show_mainmenu_view):
        self._root = root
        self._show_mainmenu_view = show_mainmenu_view
        self._frame = None
        self._diff = None

        self._start()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initiate_easy(self):
        self._diff = "easy"
        game_service.update_game_data(self._diff)
        self._screensize = (300, 300)
        self._board = Board(self._diff)
        self._game = Game(self._board, self._screensize)
        self._game.start()

    def _initiate_medium(self):
        self._diff = "medium"
        game_service.update_game_data(self._diff)
        self._screensize = (540, 540)
        self._board = Board(self._diff)
        self._game = Game(self._board, self._screensize)
        self._game.start()

    def _initiate_hard(self):
        self._diff = "hard"
        game_service.update_game_data(self._diff)
        self._screensize = (720, 720)
        self._board = Board(self._diff)
        self._game = Game(self._board, self._screensize)
        self._game.start()

    def _suspend(self):
        self._show_end_view

    def _start(self):
        self._frame = ttk.Frame(master=self._root)

        self.label = ttk.Label(master=self._frame, text="Choose game difficulty to start a game:")

        self.button5 = ttk.Button(
            master=self._frame, text="Main menu", command=self._show_mainmenu_view)

        self.button1 = ttk.Button(
            master=self._frame, text="Easy", command=self._initiate_easy)
        self.button2 = ttk.Button(
            master=self._frame, text="Medium", command=self._initiate_medium)
        self.button3 = ttk.Button(
            master=self._frame, text="Hard", command=self._initiate_hard)

        self.label.grid(row=1, column=1, pady=10)
        self.button1.grid(row=3, column=0, pady=10)
        self.button2.grid(row=3, column=1, pady=10)
        self.button3.grid(row=3, column=2, pady=10)
        self.button5.grid(row=7, column=1, pady=30)

        self._frame.grid_columnconfigure(0, weight=2, minsize=250)
        self._frame.grid_columnconfigure(1, weight=2, minsize=250)
        self._frame.grid_columnconfigure(2, weight=2, minsize=250)
