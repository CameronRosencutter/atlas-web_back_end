#!/usr/bin/env python3
"""This will be used to test utilities.
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """this is the testaccessnestedmap class"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """this will check for the correct results"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        ({}, ("a",), "Key 'a' not found in nested map"),
        ({"a": 1}, ("a", "b"), "Key 'b' not found in nested map"),
    ])
    def test_access_nested_map_exception(
            self, nested_map, path, expected_exception_message):
        """validates if everything is correct"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestMemoize(unittest.TestCase):
"""This is the testmemoize class"""
    class TestClass:

        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()

    def test_memoize(self):
        # Create an instance of the TestClass
        test_instance = self.TestClass()

        # Mock the a_method using unittest.mock.patch
        with patch.object(test_instance, 'a_method', 
                          return_value=42) as mock_method:
            # Call a_property twice
            result1 = test_instance.a_property()
            result2 = test_instance.a_property()

            # Assert that a_method is only called once
            mock_method.assert_called_once()

            # Assert that the results are correct
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)


if __name__ == '__main__':
    unittest.main()
