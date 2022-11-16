from tkinter import Tk, ttk, StringVar, constants
from services.login_service import login_service, InvalidCredentialsError

class LoginView:
    def __init__(self, root, handle_login, handle_show_createuser_view):
        self._root = root
        self._handle_login = handle_login
        self._handle_show_createuser_view = handle_show_createuser_view
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._error_variable = None
        self._error_label = None

        self._start()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _login_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        try:
            login_service.login(username, password)
            self._handle_login()
        except InvalidCredentialsError:
            self._show_error("Invalid username or password")

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _start(self):
        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
        )

        self._error_label.grid()

        self.username_label = ttk.Label(master=self._frame, text="Username")
        self._username_entry = ttk.Entry(master=self._frame)

        self.password_label = ttk.Label(master=self._frame, text="Password")
        self._password_entry = ttk.Entry(master=self._frame)
        self.button1 = ttk.Button(master=self._frame, text="Log in", command=self._login_handler)
        self.button2 = ttk.Button(master=self._frame, text="Create user", command=self._handle_show_createuser_view)
        self.button3 = ttk.Button(master=self._frame, text="Quit", command=self._root.destroy)

        self.username_label.grid(row=1, column=1, pady=10)
        self._username_entry.grid(row=2, column=1)

        self.password_label.grid(row=3, column=1, pady=10)
        self._password_entry.grid(row=4, column=1)

        self.button1.grid(row=5, column=1, pady=10)

        self.button2.grid(row=6, column=1, pady=10)

        self.button3.grid(row=7, column=1, pady=10)

        self._root.grid_columnconfigure(1, weight=1, minsize=300)

        self._hide_error()