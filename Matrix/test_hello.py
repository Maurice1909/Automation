import unittest

from Matrix.hello import greeting   

class TestGreeting(unittest.TestCase):
    def test_greeting(self):
        self.assertEqual(greeting(), "Hello, World!")