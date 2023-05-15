#!/usr/bin/python3
""" Unit test for user model """
import unittest
from models.state import State

class TestUser(unittest.TestCase):
    
    def test_uid(self):
        self.assertEquals(type(State.id), type("hello"))

