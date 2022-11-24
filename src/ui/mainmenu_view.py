from tkinter import ttk, constants
from services.login_service import login_service

class MainmenuView:
    def __init__(self, root, show_login_view, show_highscore_view_easy, show_play_view):

        self._root = root
        self._frame = None
        self._show_login_view = show_login_view
        self._show_highscore_view_easy = show_highscore_view_easy
        self._show_play_view = show_play_view
        self._user = login_service.get_current_user()

        self._start()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _start(self):
        self._frame = ttk.Frame(master=self._root)

        name = self._user.username
        self.welcome_label = ttk.Label(master=self._frame, text="Welcome, " + str(name))

        self.button1 = ttk.Button(master=self._frame, text="Play", command=self._show_play_view)
        self.button2 = ttk.Button(master=self._frame, text="High scores", command=self._show_highscore_view_easy)
        self.button3 = ttk.Button(master=self._frame, text="Change user", command=self._show_login_view)
        self.button4 = ttk.Button(master=self._frame, text="Quit", command=self._root.destroy)

        self.welcome_label.grid(row=1, column=1, pady=10)

        self._frame.grid_columnconfigure(1, weight=1, minsize=700)

        self.button1.grid(row=3, column=1, pady=50)

        self.button2.grid(row=4, column=1, pady=50)

        self.button3.grid(row=5, column=1, pady=50)

        self.button4.grid(row=6, column=1, pady=75)