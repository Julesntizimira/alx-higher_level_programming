#!/usr/bin/python3
'''this is unittest module for 6-max_integer module'''


import unittest
max_integer = __import__('6-max_integer').max_integer

class Testmax(unittest.TestCase):
    
    def test_max(self):
        """Test with an regular list
           Return maximum number
        """
        lst = [3,6,9,10,8,22,6]
        result = max_integer(lst)
        self.assertEqual(result, 22)

    def test_not_int(self):
        """Test a list with non-int type elements
           should raise a TypeError exception
        """
        lst = ["a", "b", 9]
        self.assertRaises(TypeError, max_integer, lst)

    def test_empty(self):
        """Test with an empty list
           Return None
        """
        lst = []
        result = max_integer(lst)
        self.assertEqual(result, None)

    def test_negative(self):
        """Test with a list of negative elements:
           Return the max
        """
        lst = [-4, -8, -2]
        result = max_integer(lst)
        self.assertEqual(result, -2)

    def test_float(self):
        """Test with a list of mixed ints and floats
           Return the max
        """
        lst = [1, 6.5, 4]
        result = max_integer(lst)
        self.assertEqual(result, 6.5)

    def test_not_list(self):
        """Test with a parameter , not list
           raise a TypeError
        """
        self.assertRaises(TypeError, max_integer, 5)

    def test_unique(self):
        """Test with a list of one int
           return ithe value of this int
        """
        lst = [52]
        result = max_integer(lst)
        self.assertEqual(result, 52)

    def test_identical(self):
        """Test with a list of identical elements
           return the value
        """
        lst = [5, 5, 5, 5, 5]
        result = max_integer(lst)
        self.assertEqual(result, 5)

    def test_strings(self):
        """Test with a list of strings
           return the first string
        """
        lst = ["yey", "hello"]
        result = max_integer(lst)
        self.assertEqual(result, "yey")

    def test_none(self):
        """Test with a None as parameter
           raise a TypeError
        """
        self.assertRaises(TypeError, max_integer, None)


if __name__ == "__main__":
    unittest.main()
