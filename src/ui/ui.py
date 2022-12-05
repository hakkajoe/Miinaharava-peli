from ui.login_view import LoginView
from ui.mainmenu_view import MainmenuView
from ui.createuser_view import CreateuserView
from ui.highscores_view_easy import HighscoresViewEasy
from ui.highscores_view_medium import HighscoresViewMedium
from ui.highscores_view_hard import HighscoresViewHard
from ui.play_view import PlayView


class UI:
    """manages user interface information
    """
    def __init__(self, root):
        """constructor that creates a new interface

        Args:
            root: tkinter's TK() -class
        """
        self._root = root
        self._current_view = None

    def start(self):
        """starta processing views
        """
        self._show_login_view()

    def get_current_view(self):
        """returns information about the existence of the current view

        Returns:
            True, if view is open, else False
        """
        return self._current_view

    def _hide_current_view(self):
        """hides the current view if one is on
        """
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_login_view(self):
        """shows login page
        """
        self._hide_current_view()

        self._current_view = LoginView(
            self._root, self._show_mainmenu_view, self._show_create_user_view)

        self._current_view.pack()

    def _show_mainmenu_view(self):
        """shows main menu
        """
        self._hide_current_view()

        self._current_view = MainmenuView(
            self._root, self._show_login_view, self._show_highscore_view_easy, self._show_play_view)

        self._current_view.pack()

    def _show_create_user_view(self):
        """shows view for creating a new user
        """
        self._hide_current_view()

        self._current_view = CreateuserView(
            self._root, self._show_mainmenu_view, self._show_login_view)

        self._current_view.pack()

    def _show_highscore_view_easy(self):
        """shows the page with the best results of the easiest difficulty level
        """
        self._hide_current_view()

        self._current_view = HighscoresViewEasy(
            self._root, self._show_mainmenu_view, self._show_highscore_view_medium, self._show_highscore_view_hard)

        self._current_view.pack()

    def _show_highscore_view_medium(self):
        """shows the page with the best results of medium difficulty
        """
        self._hide_current_view()

        self._current_view = HighscoresViewMedium(
            self._root, self._show_mainmenu_view, self._show_highscore_view_easy, self._show_highscore_view_hard)

        self._current_view.pack()

    def _show_highscore_view_hard(self):
        """shows the page with the best results of the hardest difficulty
        """
        self._hide_current_view()

        self._current_view = HighscoresViewHard(
            self._root, self._show_mainmenu_view, self._show_highscore_view_easy, self._show_highscore_view_medium)

        self._current_view.pack()

    def _show_play_view(self):
        """shows the page where you select the game's difficulty level and start the game
        """
        self._hide_current_view()

        self._current_view = PlayView(
                self._root, self._show_mainmenu_view)

        self._current_view.pack()