from tkinter import ttk, constants

class MainmenuView:
    def __init__(self, root):

        self._root = root
        self._frame = None

        self._start()

    def _start(self):
        self._frame = ttk.Frame(master=self._root)

        self.button1 = ttk.Button(master=self._frame, text="Play")
        self.button2 = ttk.Button(master=self._frame, text="High scores")
        self.button3 = ttk.Button(master=self._frame, text="Quit", command=self._root.destroy)

        self.button1.grid(row=5, column=1, pady=50)

        self.button2.grid(row=6, column=1, pady=50)

        self.button3.grid(row=7, column=1, pady=50)

        self._root.grid_columnconfigure(1, weight=1, minsize=300)