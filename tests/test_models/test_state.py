#!/usr/bin/python3
"""Testing state module"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """Testing State class"""

    def __init__(self, *args, **kwargs):
        """Initializes data"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """Testing name attributte"""
        new = self.value()
        self.assertEqual(type(new), self.value)
