from entities.highscores import Highscore
from database_connection import get_database_connection

class ScoreRepository:
    """manages score data between score_service file and database file
    """

    def __init__(self, connection):
        """sets up connection to database

        Args:
            connection: database connection
        """

        self._connection = connection

    def find_all_easy(self):
        """gets 10 top easy scores from database

        Returns:
            list, top 10 easy scores
        """

        cursor = self._connection.cursor()

        result = cursor.execute(
            "select score, username, date from scores where diff = 'easy' order by score limit 10"
            ).fetchall()
        
        return result

    def find_all_medium(self):
        """gets 10 top medium scores from database

        Returns:
            list, top 10 medium scores
        """

        cursor = self._connection.cursor()

        result = cursor.execute(
            "select score, username, date from scores where diff = 'medium' order by score limit 10"
            ).fetchall()

        return result

    def find_all_hard(self):
        """gets 10 top hard scores from database

        Returns:
            list, top 10 hard scores
        """

        cursor = self._connection.cursor()

        result = cursor.execute(
            "select score, username, date from scores where diff = 'hard' order by score limit 10"
            ).fetchall()

        return result

    def create(self, entry):
        """creates a new score entry to score database

        Args:
            entry (Highscore): contains all info of Highscore entry
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "insert or replace into scores (score, username, date, diff) values (?, ?, ?, ?)",
            (entry.score, entry.username, entry.date, entry.diff)
        )

        self._connection.commit()

    def delete_all(self):
        """removes all entries from score database
        """

        cursor = self._connection.cursor()

        cursor.execute("delete from scores")

        self._connection.commit()


score_repository = ScoreRepository(get_database_connection())
