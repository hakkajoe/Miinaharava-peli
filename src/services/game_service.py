from datetime import datetime
from services.login_service import login_service
from services.score_service import score_service

class GameService:
    """handles data related to current game
    """

    def __init__(self):
        """sets up game data
        """
        self._user = None
        self._date = None
        self._diff = None
        self._score = None
        self._status = None
    
    def update_game_data(self, diff):
        """sets part of the final game data (data that can be gathered at the start of the game)

        Args:
            diff: game difficulty
        """
        user = login_service.get_current_user()
        self._user = user.username
        self._date = datetime.now().strftime('%d.%m.%Y')
        self._diff = diff
    
    def register_game_data(self, score, status):
        """sets rest of game data and sends it to database if score was given

        Args:
            score: game score
            status: won or lost
        """
        self._score = score
        self._status = status
        if self._score > 0:
            score_service.create_score(self._score, self._user, self._date, self._diff)
        self.reset_data()

    def reset_data(self):
        """resets game data
        """
        self._user = None
        self._date = None
        self._diff = None
        self._score = None
        self._status = None

game_service = GameService()