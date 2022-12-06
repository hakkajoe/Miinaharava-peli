from entities.highscores import Highscore
from repositories.score_repository import (
    score_repository as default_score_repository)

class ScoreService:
    """Handles retrieving and sending score data
    """
    def __init__(self, score_repository=default_score_repository):
        """sets up connection to repository

        Args:
            user_repository (optional): name of repository.
        """
        self._score = None
        self._score_repository = score_repository

    def get_scores(self, diff):
        """retrieve info of all scores
        
        Args:
            diff: difficulty of scores fetched from repository

        Returns:
            list, all scores in repository, by requested difficulty
        """
        if diff == "easy":
            return self._score_repository.find_all("easy")
        if diff == "medium":
            return self._score_repository.find_all("medium")
        if diff == "hard":
            return self._score_repository.find_all("hard")

    def create_score(self, score, username, date, diff):
        """creates a new score

        Args:
            score: game score
            username: user who achieved the score
            date: date when score was achieved
            diff: difficulty of game
        """

        self._score_repository.create(Highscore(score, username, date, diff))


score_service = ScoreService()
