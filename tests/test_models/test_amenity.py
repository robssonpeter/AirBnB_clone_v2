#!/usr/bin/python3
""" Unit test for user model """
import unittest
from models.amenity import Amenity

class TestUser(unittest.TestCase):
    
    def test_uid(self):
        self.assertEquals(type(Amenity.id), type("hello"))

