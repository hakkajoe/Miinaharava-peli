import unittest
from repositories.user_repository import user_repository
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.user_1 = User('esimerkkikäyttäjä1', '12345')
        self.user_2 = User('Dhfdwihce68631', 'cdbschbw372987324')

    def test_create(self):
        user_repository.create(self.user_1)
        users = user_repository.find_all()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, self.user_1.username)

    def test_find_all(self):
        user_repository.create(self.user_1)
        user_repository.create(self.user_2)
        users = user_repository.find_all()

        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].username, self.user_1.username)
        self.assertEqual(users[1].username, self.user_2.username)

    def test_find_by_username(self):
        user_repository.create(self.user_1)

        user = user_repository.find_by_username(self.user_1.username)

        self.assertEqual(user.username, self.user_1.username)
