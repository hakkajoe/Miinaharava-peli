from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository)


class InvalidCredentialsError(Exception):
    pass


class UsernameExistsError(Exception):
    pass


class LoginService:
    """Handles retrieving and sending user data
    """

    def __init__(self, user_repository=default_user_repository):
        """sets up connection to repository

        Args:
            user_repository (optional): name of repository.
        """
        self._user = None
        self._user_repository = user_repository

    def login(self, username, password):
        """handles logging in

        Args:
            username: given username
            password: given password

        Raises:
            InvalidCredentialsError: if user is not found

        Returns:
            User, if user was found
        """

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise InvalidCredentialsError("Invalid username or password")

        self._user = user

        return user

    def get_current_user(self):
        """retrieve info of current logged in user

        Returns:
            User
        """
        return self._user

    def get_users(self):
        """retrieve info of all users

        Returns:
            list, all user info found in user database
        """
        return self._user_repository.find_all()

    def logout(self):
        """logs current user out
        """
        self._user = None

    def create_user(self, username, password, login=True):
        """creates a new user

        Args:
            username: given username
            password: given password
            login (optional): sets whether the new created user will be automatically logged in

        Raises:
            UsernameExistsError: if username is already found in database

        Returns:
            User
        """

        existing_user = self._user_repository.find_by_username(username)

        if existing_user:
            raise UsernameExistsError(f"Username {username} already exists")

        user = self._user_repository.create(User(username, password))

        if login:
            self._user = user

        return user


login_service = LoginService()
