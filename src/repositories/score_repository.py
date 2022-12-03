from entities.highscores import Highscore
from database_connection import get_database_connection


def get_score_by_row(row):
    return Highscore(row["score"], row["username"], row["date"], row["diff"]) if row else None


class ScoreRepository:

    def __init__(self, connection):

        self._connection = connection

    def find_all_easy(self):

        cursor = self._connection.cursor()

        result = cursor.execute(
            "select score, username, date from scores where diff = 'easy' order by score limit 10"
            ).fetchall()
        
        return result

    def find_all_medium(self):

        cursor = self._connection.cursor()

        result = cursor.execute(
            "select score, username, date from scores where diff = 'medium' order by score limit 10"
            ).fetchall()

        return result

    def find_all_hard(self):

        cursor = self._connection.cursor()

        result = cursor.execute(
            "select score, username, date from scores where diff = 'hard' order by score limit 10"
            ).fetchall()

        return result

    def create(self, entry):

        cursor = self._connection.cursor()

        cursor.execute(
            "insert or replace into scores (score, username, date, diff) values (?, ?, ?, ?)",
            (entry.score, entry.username, entry.date, entry.diff)
        )

        self._connection.commit()

    def delete_all(self):

        cursor = self._connection.cursor()

        cursor.execute("delete from scores")

        self._connection.commit()


score_repository = ScoreRepository(get_database_connection())
