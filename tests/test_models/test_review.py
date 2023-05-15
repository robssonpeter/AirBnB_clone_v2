#!/usr/bin/python3
""" Unit test for user model """
import unittest
from models.review import Review

class TestUser(unittest.TestCase):
    
    def test_uid(self):
        self.assertEquals(type(Review.id), type("hello"))

