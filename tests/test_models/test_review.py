#!/usr/bin/python3
"""Testing Review module"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """Testing review class  """

    def __init__(self, *args, **kwargs):
        """Initializes data"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """Testing place_id attribute"""
        new = self.value()
        self.assertEqual(type(new), self.value)

    def test_user_id(self):
        """Testing user_id attribute"""
        new = self.value()
        self.assertEqual(type(new), self.value)

    def test_text(self):
        """Testing text attribute"""
        new = self.value()
        self.assertEqual(type(new), self.value)
