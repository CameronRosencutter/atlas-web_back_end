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


class TestGetJson(unittest.TestCase):
    """This is the testgetjson function"""
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, url, expected_payload, mock_requests_get):
        """Test the get_json function."""
        # Set up the mock response
        response_mock = Mock()
        response_mock.json.return_value = expected_payload
        mock_requests_get.return_value = response_mock

        # Call the get_json function
        result = get_json(url)

        # Assertions
        self.assertEqual(result, expected_payload)
        mock_requests_get.assert_called_once_with(url)
        response_mock.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    '''Inherits from testcase,
        unittest class for memoize
        function'''
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

    def test_memoize(self
                     ) -> None:
        '''Method asserts that output of
            memoize is as expected'''

        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method',
                          return_value=42) as mock_method:
            instance = TestClass()
            self.assertEqual(instance.a_property,
                             mock_method.return_value)
            self.assertEqual(instance.a_property,
                             mock_method.return_value)
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
