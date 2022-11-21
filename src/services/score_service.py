from entities.highscores import Highscore
from repositories.score_repository import (score_repository as default_score_repository)

class NoScoreExistsError(Exception):
    pass


class ScoreService:

    def __init__(self, score_repository=default_score_repository):
        self._score = None
        self._score_repository = score_repository

    def get_scores(self):
        return self._score_repository.find_all()

    def create_score(self, username, score, date):

        self._score_repository.create(Highscore(username, score, date))

score_service = ScoreService()