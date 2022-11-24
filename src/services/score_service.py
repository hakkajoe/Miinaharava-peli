from entities.highscores import Highscore
from repositories.score_repository import (score_repository as default_score_repository)

class NoScoreExistsError(Exception):
    pass


class ScoreService:

    def __init__(self, score_repository=default_score_repository):
        self._score = None
        self._score_repository = score_repository

    def get_scores_easy(self):
        return self._score_repository.find_all_easy()

    def get_scores_medium(self):
        return self._score_repository.find_all_medium()

    def get_scores_hard(self):
        return self._score_repository.find_all_hard()

    def create_score(self, username, score, date, diff):

        self._score_repository.create(Highscore(username, score, date, diff))

score_service = ScoreService()