import unittest
from entities.user import User
from services.login_service import InvalidCredentialsError, UsernameExistsError, login_service
from repositories.user_repository import user_repository as default_user_repository

class TestLoginService(unittest.TestCase):
    def setUp(self, user_repository=default_user_repository):
        user_repository.delete_all()
        self.user_1 = User('esimerkkikäyttäjä1', '12345')
        self.user_2 = User('Dhfdwihce68631', 'cdbschbw372987324')
        self.user_3 = User('esimerkkikäyttäjä1', '12345')
        self._user = None
        self._user_repository = user_repository

    def test_login_get_current_user_logout(self):
        self._user_repository.create(self.user_1)
        user = login_service.login(self.user_1.username, self.user_1.password)
        self._user = user
        self.assertEqual(self._user.username, 'esimerkkikäyttäjä1')
        data = login_service.get_current_user()
        self.assertEqual(data.username, self.user_1.username)
        login_service.logout()
        data = login_service.get_current_user()
        self.assertEqual(data, None)

    def test_login_no(self):
        self.assertRaises(InvalidCredentialsError, login_service.login, self.user_1.username, self.user_1.password)

    def test_get_users(self):
        self._user_repository.create(self.user_1)
        self._user_repository.create(self.user_2)
        data = login_service.get_users()
        self.assertEqual(len(data), 2)

    def test_create_user_yes(self):
        login_service.create_user(self.user_1.username, self.user_1.password)
        data = login_service.get_current_user()
        self.assertEqual(data.username, self.user_1.username)

    def test_create_user_no(self):
        login_service.create_user(self.user_1.username, self.user_1.password)
        login_service.logout()
        self.assertRaises(UsernameExistsError, login_service.create_user, self.user_3.username, self.user_3.password)