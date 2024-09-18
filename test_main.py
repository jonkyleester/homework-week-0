# test_main.py
import unittest
from main import greet_person, hello_world 

class TestHelloWorld(unittest.TestCase):


    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello from Jon Ester!")

    def test_greet_person(self):
        name = "Jon"
        self.assertEqual(greet_person(name), "Hello, [name]!")

if __name__ == '__main__':
    unittest.main()

