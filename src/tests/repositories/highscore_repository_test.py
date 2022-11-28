import unittest
from repositories.score_repository import score_repository
from entities.highscores import Highscore


class TestHighscoreRepository(unittest.TestCase):
    def setUp(self):
        score_repository.delete_all()
        self.score_1 = Highscore(123, 'matti', '1.1.2000', 'easy')
        self.score_2 = Highscore(1000, 'maija', '21.12.2022', 'medium')
        self.score_3 = Highscore(500, 'milla', '30.9.2030', 'medium')

    def test_create(self):
        score_repository.create(self.score_1)
        scores = score_repository.find_all_easy()

        self.assertEqual(len(scores), 1)
        self.assertEqual(scores[0], (self.score_1.score, self.score_1.username, self.score_1.date))

    def test_find_all_easy(self):
        score_repository.create(self.score_1)
        score_repository.create(self.score_2)
        score_repository.create(self.score_3)
        scores = score_repository.find_all_easy()

        self.assertEqual(len(scores), 1)
        self.assertEqual(scores[0], (self.score_1.score, self.score_1.username, self.score_1.date))

    def test_find_all_medium(self):
        score_repository.create(self.score_1)
        score_repository.create(self.score_2)
        score_repository.create(self.score_3)
        scores = score_repository.find_all_medium()

        self.assertEqual(len(scores), 2)
        self.assertEqual(scores[0], (self.score_3.score, self.score_3.username, self.score_3.date))
        self.assertEqual(scores[1], (self.score_2.score, self.score_2.username, self.score_2.date))

    def test_find_all_hard(self):
        score_repository.create(self.score_1)
        score_repository.create(self.score_2)
        score_repository.create(self.score_3)
        scores = score_repository.find_all_hard()

        self.assertEqual(len(scores), 0)