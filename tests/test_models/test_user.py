#!/usr/bin/python3
""" Unit test for user model """
import unittest
from models.user import User

class TestUser(unittest.TestCase):
    
    def test_uid(self):
        self.assertEquals(type(User.id), type("hello"))

    def test_email(self):
        self.assertEquals("@" in User.email, True)

    def test_password(self):
        self.assertEquals(type(User.password), type("hello"))

    def test_first_name(self):
        self.assertEquals(type(User.first_name), type("hello"))

    def test_last_name(self):
        self.assertEquals(type(User.last_name), type("hello"))

