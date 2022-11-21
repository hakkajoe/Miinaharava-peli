from database_connection import get_database_connection
from services.score_service import score_service
from tkinter import constants, ttk

class HighscoresView:
    def __init__(self, root, show_mainmenu_view):

        self._root = root
        self._frame = None
        self._show_mainmenu_view = show_mainmenu_view
        self._scores = score_service.get_scores()

        self._start()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _start(self):
        self._frame = ttk.Frame(master=self._root)

        if len(self._scores) == 0:
            self.intro_label = ttk.Label(master=self._frame, text="No scores available")
        else:
            self.intro_label = ttk.Label(master=self._frame, text="Top 10:")
            self.intro_score_label = ttk.Label(master=self._frame, text="Score:")
            self.intro_user_label = ttk.Label(master=self._frame, text="User:")
            self.intro_date_label = ttk.Label(master=self._frame, text="Achieved:")
            index = 3
            for i in self._scores:
                self.score_label = ttk.Label(master=self._frame, text=i[0])
                self.user_label = ttk.Label(master=self._frame, text=i[1])
                self.date_label = ttk.Label(master=self._frame, text=i[2])
                self.score_label.grid(row=index, column=0, pady=25)
                self.user_label.grid(row=index, column=1, pady=25)
                self.date_label.grid(row=index, column=2, pady=25)
                index += 1

        self.intro_label.grid(row=1, column=1, pady=10)
        self.intro_score_label.grid(row=2, column=0, pady=10)
        self.intro_user_label.grid(row=2, column=1, pady=10)
        self.intro_date_label.grid(row=2, column=2, pady=10)

        self.button = ttk.Button(master=self._frame, text="Back", command=self._show_mainmenu_view)

        self._frame.grid_columnconfigure(0, weight=2, minsize=250)
        self._frame.grid_columnconfigure(1, weight=2, minsize=250)
        self._frame.grid_columnconfigure(2, weight=2, minsize=250)

        self.button.grid(row=12, column=1, pady=50)