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

    def find_all(self, diff):
        """gets 10 top scores from database

        Args:
            diff: difficulty of scores fetched

        Returns:
            list, top 10 scores of given difficulty
        """

        cursor = self._connection.cursor()

        result = cursor.execute(
            f"select score, username, date from scores where diff = '{diff}' order by score limit 10"
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
