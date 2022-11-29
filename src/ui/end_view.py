from tkinter import ttk, constants
from datetime import datetime
from services.score_service import score_service
from services.login_service import login_service
from services.game_service import game_service


class EndView:
    def __init__(self, root, show_play_view, show_mainmenu_view):
        self._root = root
        self._show_mainmenu_view = show_mainmenu_view
        self._show_play_view = show_play_view
        self._frame = None
        self._user = login_service.get_current_user()
        self._score_handler()

        self._start()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _score_handler(self):
        data = game_service.get_game_data()
        username = data[0]
        date = data[1]
        diff = data[2]
        self._score = data[3]
        if self._score > 0:
            score_service.create_score(self._score, username, date, diff)
        game_service.reset_data()

    def _start(self):
        self._frame = ttk.Frame(master=self._root)

        if self._score != 0:
            self.score_label = ttk.Label(master=self._frame, text="Congratulations, your score was " + str(self._score) + " seconds!")
        else:
            self.score_label = ttk.Label(master=self._frame, text="Better luck next time!")

        self.button1 = ttk.Button(
            master=self._frame, text="Play again", command=self._show_play_view)

        self.button2 = ttk.Button(
            master=self._frame, text="Main menu", command=self._show_mainmenu_view)

        self.score_label.grid(row=1, column=1, pady=10)

        self.button1.grid(row=4, column=1, pady=10)
        self.button2.grid(row=5, column=1, pady=10)

        self._frame.grid_columnconfigure(0, weight=2, minsize=250)
        self._frame.grid_columnconfigure(1, weight=2, minsize=250)
        self._frame.grid_columnconfigure(2, weight=2, minsize=250)
