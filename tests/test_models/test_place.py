#!/usr/bin/python3
"""Testing place module"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """Testing PLace class"""

    def __init__(self, *args, **kwargs):
        """Initilizes data"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """Testing city_id attribute"""
        new = self.value()
        self.assertEqual(type(new), self.value)

    def test_user_id(self):
        """Testing user_id attribute """
        new = self.value()
        self.assertEqual(type(new), self.value)

    def test_name(self):
        """Testing name attribute """
        new = self.value()
        self.assertEqual(type(new), self.value)

    def test_description(self):
        """Testing description attribute"""
        new = self.value()
        self.assertEqual(type(new), self.value)

    def test_number_rooms(self):
        """Testing number of rooms attribute """
        new = self.value()
        self.assertEqual(type(new), self.value)

    def test_number_bathrooms(self):
        """Testing number of bathrooms attribute"""
        new = self.value()
        self.assertEqual(type(new), self.value)

    def test_max_guest(self):
        """Testing max guest attribute """
        new = self.value()
        self.assertEqual(type(new), self.value)

    def test_price_by_night(self):
        """Testing price by night attribute"""
        new = self.value()
        self.assertEqual(type(new), self.value)

    def test_latitude(self):
        """Testing latitude attribute """
        new = self.value()
        self.assertEqual(type(new), self.value)

    def test_longitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new), self.value)

    def test_amenity_ids(self):
        """ """
        new = self.value()
        self.assertEqual(type(new), self.value)
