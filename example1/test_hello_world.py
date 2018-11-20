import unittest
from example1.hello_world import hello_world


class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), 'Hello, world!!')
