from datetime import datetime
from services.login_service import login_service

class GameService:

    def __init__(self):
        self._user = None
        self._date = None
        self._diff = None
        self._score = None
        self._status = None

    def get_game_data(self):
        data = []
        data.append(self._user)
        data.append(self._date)
        data.append(self._diff)
        data.append(self._score)
        data.append(self._status)
        return data
    
    def update_game_data1(self, diff):
        user = login_service.get_current_user()
        self._user = user.username
        self._date = datetime.now().strftime('%d.%m.%Y')
        self._diff = diff
    
    def update_game_data2(self, score, status):
        self._score = score
        self._status = status

    def reset_data(self):
        self._user = None
        self._date = None
        self._diff = None
        self._score = None
        self._status = None

game_service = GameService()