#!/usr/bin/python3
"""Test for amenity module"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """Test Amenity class """

    def __init__(self, *args, **kwargs):
        """Initializes data """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Testing name attribute """
        new = self.value()
        self.assertEqual(type(new), self.value)
