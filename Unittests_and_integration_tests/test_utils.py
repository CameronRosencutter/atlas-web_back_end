#!/usr/bin/env python3
"""This will be used to test utilities.
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize

class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError, "Key 'a' not found in the nested map."),
        ({"a": 1}, ("a", "b"), KeyError, "Key 'b' not found in the nested map."),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_exception, expected_message):
        with self.assertRaises(expected_exception) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception), expected_message)

class TestGetJson(unittest.TestCase):
    """ TestGetJson class for utils.py
    Args:
        unittest (unittest.TestCase): Unit testing for utils.py
    """
    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """ Test get_json method for utils.py
        check if the method returns the result as expected
        """
        # mock the get_json function
        mock = Mock()
        # set the return value of the mock
        mock.json.return_value = test_payload
        # patch the requests.get to return the mock response object
        with patch('requests.get') as mock_get:
            # set the return value of the mock
            mock_get.return_value = mock
            # call the function using the test_url
            result = get_json(test_url)
            self.assertEqual(result, test_payload)
            # assert that the mock was called once with the test_url
            mock_get.assert_called_once_with(test_url)