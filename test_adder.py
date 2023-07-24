import unittest
from adder import add_me


class MyTestCase(unittest.TestCase):
    def test_add_me_positive_arguments(self):
        self.assertEqual(9, add_me(7, 2))

    def test_add_me_negative_arguments(self):
        self.assertEqual(-5, add_me(-2, -3))


if __name__ == '__main__':
    unittest.main()
