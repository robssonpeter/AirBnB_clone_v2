#!/usr/bin/python3
""" Unit test for user model """
import unittest
from models.city import City

class TestUser(unittest.TestCase):
    
    def test_uid(self):
        self.assertEquals(type(City.id), type("hello"))

