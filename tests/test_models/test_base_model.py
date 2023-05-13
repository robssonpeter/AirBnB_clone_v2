import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_uuid(self):
        self.assertEqual(type(BaseModel.id), type("hello"))
