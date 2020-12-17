#!/usr/bin/python3
"""Testing user module"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """Testing User class"""

    def __init__(self, *args, **kwargs):
        """Initilizes data"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """Testing first name attribute"""
        new = self.value()
        self.assertEqual(type(new), self.value)

    def test_last_name(self):
        """Testing last name attribute """
        new = self.value()
        self.assertEqual(type(new), self.value)

    def test_email(self):
        """Testing email attribute """
        new = self.value()
        self.assertEqual(type(new), self.value)

    def test_password(self):
        """Testing password attribute """
        new = self.value()
        self.assertEqual(type(new), self.value)
