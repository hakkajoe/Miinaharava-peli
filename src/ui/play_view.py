from tkinter import ttk, StringVar, constants
from services.score_service import score_service
from services.login_service import login_service
from datetime import datetime
from game.game import Game
from game.board import Board

class PlayView:
    def __init__(self, root, show_mainmenu_view):
        self._root = root
        self._show_mainmenu_view = show_mainmenu_view
        self._frame = None
        self._test_entry = None
        self._user = login_service.get_current_user()

        self._start()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _score_handler(self):
        score = self._test_entry.get()
        username = self._user.username
        date = datetime.now().strftime('%d.%m.%Y')

        score_service.create_score(score, username, date)

    def _initiate_easy(self):
        self._size = (10,10)
        self._screensize = (300,300)
        self._prob = 0.1
        self._bombs = 10
        self._board = Board(self._size, self._prob)
        self._game = Game(self._board, self._screensize)
        self._game.run()

    def _initiate_medium(self):
        self._size = (18,18)
        self._screensize = (540,540)
        self._prob = 0.1
        self._bombs = 43
        self._board = Board(self._size, self._prob)
        self._game = Game(self._board, self._screensize)
        self._game.run()

    def _initiate_hard(self):
        self._size = (24,24)
        self._screensize = (720,720)
        self._prob = 0.1
        self._bombs = 120
        self._board = Board(self._size, self._prob)
        self._game = Game(self._board, self._screensize)
        self._game.run()

    def _start(self):
        self._frame = ttk.Frame(master=self._root)

        self.test_label = ttk.Label(master=self._frame, text="Test score")
        self._test_entry = ttk.Entry(master=self._frame)

        self.button4 = ttk.Button(master=self._frame, text="Submit", command=self._score_handler)

        self.button5 = ttk.Button(master=self._frame, text="Main menu", command=self._show_mainmenu_view)

        self.button1 = ttk.Button(master=self._frame, text="Easy", command=self._initiate_easy)
        self.button2 = ttk.Button(master=self._frame, text="Medium", command=self._initiate_medium)
        self.button3 = ttk.Button(master=self._frame, text="Hard", command=self._initiate_hard)

        self.test_label.grid(row=1, column=1, pady=10)
        self._test_entry.grid(row=2, column=1)

        self.button1.grid(row=3, column=0, pady=10)
        self.button2.grid(row=3, column=1, pady=10)
        self.button3.grid(row=3, column=2, pady=10)
        self.button4.grid(row=5, column=1, pady=10)
        self.button5.grid(row=7, column=1, pady=30)

        self._frame.grid_columnconfigure(0, weight=2, minsize=250)
        self._frame.grid_columnconfigure(1, weight=2, minsize=250)
        self._frame.grid_columnconfigure(2, weight=2, minsize=250)