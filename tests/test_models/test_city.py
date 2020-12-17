#!/usr/bin/python3
"""Test for City module"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """Testint city class """

    def __init__(self, *args, **kwargs):
        """Initializes data """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Testing attibute state_id """
        new = self.value()
        self.assertEqual(type(new), self.value)

    def test_name(self):
        """Tensting attribute name """
        new = self.value()
        self.assertEqual(type(new), self.value)
