#!/usr/bin/python3
""" Unit test for user model """
import unittest
from models.user import User

class TestUser(unittest.TestCase):
    
    def test_uid(self):
        self.assertEquals(type(User.id), type("hello"))

