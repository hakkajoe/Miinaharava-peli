from tkinter import ttk, StringVar, constants
from services.login_service import login_service, UsernameExistsError


class CreateuserView:

    def __init__(self, root, handle_create_user, handle_show_login_view):

        self._root = root
        self._handle_create_user = handle_create_user
        self._handle_show_login_view = handle_show_login_view
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _create_user_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        if len(username) == 0 or len(password) == 0:
            self._show_error("Username and password is required")
            return

        try:
            login_service.create_user(username, password)
            self._handle_create_user()
        except UsernameExistsError:
            self._show_error(f"Username {username} already exists")

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable)

        self._error_label.grid(column=1, padx=5, pady=5)

        username_label = ttk.Label(master=self._frame, text="Username")
        self._username_entry = ttk.Entry(master=self._frame)
        username_label.grid(row=1, padx=5, pady=5)
        self._username_entry.grid(row=2, padx=5, pady=5)

        password_label = ttk.Label(master=self._frame, text="Password")
        self._password_entry = ttk.Entry(master=self._frame)
        password_label.grid(row=3, padx=5, pady=5)
        self._password_entry.grid(row=4, padx=5, pady=5)

        create_user_button = ttk.Button(master=self._frame, text="Create user", command=self._create_user_handler)

        login_button = ttk.Button(master=self._frame, text="Return", command=self._handle_show_login_view)

        self._frame.grid_columnconfigure(0, weight=1, minsize=300)

        create_user_button.grid(row=5, padx=5, pady=5)
        login_button.grid(row=6, padx=5, pady=5)

        self._hide_error()