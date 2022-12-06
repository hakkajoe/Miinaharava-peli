from database_connection import get_database_connection
from services.score_service import score_service
from tkinter import constants, ttk


class HighscoresViewEasy:
    """handles actions in the easy highscore view interface
    """
    def __init__(self, root, show_mainmenu_view, show_mediumscores_view, show_hardscores_view):
        """sets up interface

        Args:
            root: contains tkinter info
            show_mainmenu_view: info needed for showing main menu view
            show_mediumscores_view: info needed for showing medium highscore view
            show_hardscores_view: info needed for showing hard highscore view
        """
        self._root = root
        self._frame = None
        self._show_mainmenu_view = show_mainmenu_view
        self._show_mediumscores_view = show_mediumscores_view
        self._show_hardscores_view = show_hardscores_view
        self._scores = score_service.get_scores("easy")

        self._start()

    def pack(self):
        """packs root info
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """ends current view
        """
        self._frame.destroy()

    def _start(self):
        """shows interface
        """
        self._frame = ttk.Frame(master=self._root)

        self.button1 = ttk.Button(
            master=self._frame, text="Scores (medium)", command=self._show_mediumscores_view)
        self.button2 = ttk.Button(
            master=self._frame, text="Scores (hard)", command=self._show_hardscores_view)

        if len(self._scores) == 0:
            self.intro_label = ttk.Label(
                master=self._frame, text="No scores available")
        else:
            self.intro_label = ttk.Label(
                master=self._frame, text="Top 10 (easy):")
            self.intro_score_label = ttk.Label(
                master=self._frame, text="Score:")
            self.intro_user_label = ttk.Label(master=self._frame, text="User:")
            self.intro_date_label = ttk.Label(
                master=self._frame, text="Achieved:")
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

        self.button0 = ttk.Button(
            master=self._frame, text="Back", command=self._show_mainmenu_view)

        self._frame.grid_columnconfigure(0, weight=2, minsize=250)
        self._frame.grid_columnconfigure(1, weight=2, minsize=250)
        self._frame.grid_columnconfigure(2, weight=2, minsize=250)

        self.button0.grid(row=13, column=1, pady=50)
        self.button1.grid(row=1, column=0, pady=50)
        self.button2.grid(row=1, column=2, pady=50)
