import unittest
import pygame
from game.game import Game
from game.board import Board
from services.game_service import game_service
from repositories.user_repository import user_repository
from repositories.score_repository import score_repository
from services.login_service import login_service
from entities.user import User

class TestGame(unittest.TestCase):

    def setUp(self):
        user_repository.delete_all()
        self.user_1 = User('esimerkkikäyttäjä1', '12345')
        user_repository.create(self.user_1)
        login_service.login(self.user_1.username, self.user_1.password)
        game_service.update_game_data("easy")
        self._screensize = (300, 300)
        self._board = Board("test")
        self._game = Game(self._board, self._screensize)

    def test_can_complete_game(self):
        self._game.run(pygame.MOUSEBUTTONDOWN, (100, 100))
        self.assertTrue(self._board.get_won())
        scores = score_repository.find_all_easy()
        self.assertEqual(len(scores), 1)
        self.assertEqual(scores[0][1], self.user_1.username)
        score_repository.delete_all()