from entities.user import User
from database_connection import get_database_connection


def get_user_by_row(row):
    """gets all user info based on given username

    Args:
        row: user info fetched from database

    Returns:
        User, full user info
    """
    return User(row["username"], row["password"]) if row else None


class UserRepository:
    """manages user data between score_service file and database file
    """

    def __init__(self, connection):
        """sets up connection to database

        Args:
            connection: database connection
        """
        self._connection = connection

    def find_all(self):
        """gets all users from database

        Returns:
            list: all users
        """

        cursor = self._connection.cursor()

        cursor.execute("select * from users")

        rows = cursor.fetchall()

        return list(map(get_user_by_row, rows))

    def find_by_username(self, username):
        """gets all users from database that have given username

        Args:
            username: given username

        Returns:
            User: full user info
        """
        cursor = self._connection.cursor()

        cursor.execute("select * from users where username = ?", (username,))

        row = cursor.fetchone()

        return get_user_by_row(row)

    def create(self, user):
        """creates user entry to database

        Args:
            user: given user info (name + password)

        Returns:
            User: same user info needed for logging in
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "insert into users (username, password) values (?, ?)",
            (user.username, user.password)
        )

        self._connection.commit()

        return user

    def delete_all(self):
        """deletes all user entries from repository
        """

        cursor = self._connection.cursor()

        cursor.execute("delete from users")

        self._connection.commit()


user_repository = UserRepository(get_database_connection())
