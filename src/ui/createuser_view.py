from tkinter import ttk, StringVar, constants
from services.login_service import login_service, UsernameExistsError


class CreateuserView:
    """handles actions in the create user interface
    """
    def __init__(self, root, handle_create_user, show_login_view):
        """sets up interface

        Args:
            root: tkinter info
            handle_create_user: info needed for showing main menu view
            show_login_view info needed for showing login view
        """
        self._root = root
        self._handle_create_user = handle_create_user
        self._show_login_view = show_login_view
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self):
        """packs root info
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """ends current view
        """
        self._frame.destroy()

    def _create_user_handler(self):
        """handles info needed for user creation and contacts login service
        """
        username = self._username_entry.get()
        password = self._password_entry.get()

        if len(username) == 0 or len(password) == 0:
            self._show_error("Username and password is required")
            return
        
        if len(username) > 30:
            self._show_error("Username too long")
            return

        try:
            login_service.create_user(username, password)
            self._handle_create_user()
        except UsernameExistsError:
            self._show_error(f"Username {username} already exists")

    def _show_error(self, message):
        """sets up error message if wrong log in credentials are used

        Args:
            message: error message
        """
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        """handles hiding error message
        """
        self._error_label.grid_remove()

    def _initialize(self):
        """shows interface
        """
        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame, textvariable=self._error_variable)

        self._error_label.grid(column=1, pady=10)

        username_label = ttk.Label(master=self._frame, text="Username")
        self._username_entry = ttk.Entry(master=self._frame)
        username_label.grid(column=1, row=1, pady=10)
        self._username_entry.grid(column=1, row=2, pady=10)

        password_label = ttk.Label(master=self._frame, text="Password")
        self._password_entry = ttk.Entry(master=self._frame)
        password_label.grid(column=1, row=3, pady=10)
        self._password_entry.grid(column=1, row=4, pady=10)

        create_user_button = ttk.Button(
            master=self._frame, text="Create user", command=self._create_user_handler)

        return_button = ttk.Button(
            master=self._frame, text="Return", command=self._show_login_view)

        self._frame.grid_columnconfigure(1, weight=1, minsize=700)

        create_user_button.grid(column=1, row=5, pady=10)
        return_button.grid(column=1, row=6, pady=10)

        self._hide_error()
