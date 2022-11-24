from database_connection import get_database_connection
from services.score_service import score_service
from tkinter import constants, ttk

class HighscoresViewHard:
    def __init__(self, root, show_mainmenu_view, show_easyscores_view, show_mediumscores_view):

        self._root = root
        self._frame = None
        self._show_mainmenu_view = show_mainmenu_view
        self._show_mediumscores_view = show_mediumscores_view
        self._show_easyscores_view = show_easyscores_view
        self._scores = score_service.get_scores_hard()

        self._start()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _start(self):
        self._frame = ttk.Frame(master=self._root)
        self.button1 = ttk.Button(master=self._frame, text="Scores (easy)", command=self._show_easyscores_view)
        self.button2 = ttk.Button(master=self._frame, text="Scores (medium)", command=self._show_mediumscores_view)

        if len(self._scores) == 0:
            self.intro_label = ttk.Label(master=self._frame, text="No scores available")
        else:
            self.intro_label = ttk.Label(master=self._frame, text="Top 10 (hard):")
            self.intro_score_label = ttk.Label(master=self._frame, text="Score:")
            self.intro_user_label = ttk.Label(master=self._frame, text="User:")
            self.intro_date_label = ttk.Label(master=self._frame, text="Achieved:")
            self.intro_score_label.grid(row=2, column=0, pady=10)
            self.intro_user_label.grid(row=2, column=1, pady=10)
            self.intro_date_label.grid(row=2, column=2, pady=10)
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

        self.button0 = ttk.Button(master=self._frame, text="Back", command=self._show_mainmenu_view)

        self._frame.grid_columnconfigure(0, weight=2, minsize=250)
        self._frame.grid_columnconfigure(1, weight=2, minsize=250)
        self._frame.grid_columnconfigure(2, weight=2, minsize=250)

        self.button0.grid(row=13, column=1, pady=50)
        self.button1.grid(row=1, column=0, pady=50)
        self.button2.grid(row=1, column=2, pady=50)