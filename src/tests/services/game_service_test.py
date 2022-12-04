import unittest
from datetime import datetime
from services.game_service import game_service
from services.login_service import login_service
from services.score_service import score_service
from repositories.user_repository import user_repository
from entities.user import User
from repositories.score_repository import score_repository

class TestGameService(unittest.TestCase):
    def SetUp(self):
        self._user = None
        self._date = None
        self._diff = None
        self._score = None
        self._status = None

    def test_update_register_reset_game_data(self):
        user_repository.delete_all()
        self.user_1 = User('esimerkkikäyttäjä1', '12345')
        user_repository.create(self.user_1)
        login_service.login(self.user_1.username, self.user_1.password)
        game_service.update_game_data("easy")
        game_service.register_game_data(100, "won")
        data = score_service.get_scores_easy()
        self.assertEqual(data[0][0], 100)
        score_repository.delete_all()

    def test_update_register_reset_game_data_fail(self):
        user_repository.delete_all()
        self.user_1 = User('esimerkkikäyttäjä1', '12345')
        user_repository.create(self.user_1)
        login_service.login(self.user_1.username, self.user_1.password)
        game_service.update_game_data("medium")
        game_service.register_game_data(0, "lost")
        data = score_service.get_scores_medium()
        self.assertEqual(len(data), 0)
        score_repository.delete_all()