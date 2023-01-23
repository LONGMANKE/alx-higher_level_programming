#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Class to evaluate those test cases.
    """

    def test_max_end(self):
        """Test max int of a list
        """
        _list = [1, 2, 3, 4]
        self.assertEqual(max_integer(_list), 4)

    def test_max_first(self):
        """Test max int of a list at the end
        """
        _list = [4, 1, 2, 3]
        self.assertEqual(max_integer(_list), 4)

    def test_max_middle(self):
        """Test max int in the middle of a list
        """
        _list = [1, 4, 2, 3]
        self.assertEqual(max_integer(_list), 4)

    def test_max_negative(self):
        """Checks the max negative int of a list
        """
        _list = [-1, -2, -3, -4]
        self.assertEqual(max_integer(_list), -1)

    def test_float(self):
        """Checks the max float of a list
        """
        _list = [1, 2, 3.3, 4.5]
        self.assertEqual(max_integer(_list), 4.5)

    def test_string(self):
        """Checks max int(within the list a string)
        """
        _list = [1, 2, '3', 4]
        with self.assertRaises(TypeError):
            max_integer(_list)

    def test_empty_list(self):
        """Checks the case of an empty list
        """
        _list = []
        self.assertEqual(max_integer(_list), None)

    def test_void_arg(self):
        self.assertEqual(max_integer(), None)
