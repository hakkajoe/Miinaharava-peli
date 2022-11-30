from ui.login_view import LoginView
from ui.mainmenu_view import MainmenuView
from ui.createuser_view import CreateuserView
from ui.highscores_view_easy import HighscoresViewEasy
from ui.highscores_view_medium import HighscoresViewMedium
from ui.highscores_view_hard import HighscoresViewHard
from ui.play_view import PlayView


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_login_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_login_view(self):
        self._hide_current_view()

        self._current_view = LoginView(
            self._root, self._show_mainmenu_view, self._show_create_user_view)

        self._current_view.pack()

    def _show_mainmenu_view(self):
        self._hide_current_view()

        self._current_view = MainmenuView(
            self._root, self._show_login_view, self._show_highscore_view_easy, self._show_play_view)

        self._current_view.pack()

    def _show_create_user_view(self):
        self._hide_current_view()

        self._current_view = CreateuserView(
            self._root, self._show_mainmenu_view, self._show_login_view)

        self._current_view.pack()

    def _show_highscore_view_easy(self):
        self._hide_current_view()

        self._current_view = HighscoresViewEasy(
            self._root, self._show_mainmenu_view, self._show_highscore_view_medium, self._show_highscore_view_hard)

        self._current_view.pack()

    def _show_highscore_view_medium(self):
        self._hide_current_view()

        self._current_view = HighscoresViewMedium(
            self._root, self._show_mainmenu_view, self._show_highscore_view_easy, self._show_highscore_view_hard)

        self._current_view.pack()

    def _show_highscore_view_hard(self):
        self._hide_current_view()

        self._current_view = HighscoresViewHard(
            self._root, self._show_mainmenu_view, self._show_highscore_view_easy, self._show_highscore_view_medium)

        self._current_view.pack()

    def _show_play_view(self):
        self._hide_current_view()

        self._current_view = PlayView(
                self._root, self._show_mainmenu_view)

        self._current_view.pack()