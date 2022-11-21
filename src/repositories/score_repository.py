from entities.highscores import Highscore
from database_connection import get_database_connection

def get_score_by_row(row):
    return Highscore(row["score"], row["username"], row["date"]) if row else None

class ScoreRepository:

    def __init__(self, connection):

        self._connection = connection

    def find_all(self):

        cursor = self._connection.cursor()

        result = cursor.execute("select score, username, date from scores order by score limit 10").fetchall()

        list = []

        for i in result:
            list.append((i[0], i[1], i[2]))

        return list

    def create(self, entry):

        cursor = self._connection.cursor()

        cursor.execute(
            "insert or replace into scores (score, username, date) values (?, ?, ?)",
            (entry.score, entry.username, entry.date)
        )

        self._connection.commit()

    def delete_all(self):

        cursor = self._connection.cursor()

        cursor.execute("delete from scores")

        self._connection.commit()

score_repository = ScoreRepository(get_database_connection())