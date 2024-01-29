#!/usr/bin/env python3
"""This will be used to test utilities.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError, ""),
        ({"a": 1}, ("a", "b"), KeyError, ""),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_exception, expected_message):
        with self.assertRaises(expected_exception) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception), expected_message)

class TestGetJson(unittest.TestCase):

    @patch('utils.requests.get')
    def test_get_json(self, mock_get):
        # Define test inputs
        test_cases = [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]

        # Iterate through test cases
        for test_url, test_payload in test_cases:
            # Create a mock response object
            mock_response = Mock()
            # Set the json method of the mock response to return the test payload
            mock_response.json.return_value = test_payload
            # Set the return value of the mock get method to the mock response
            mock_get.return_value = mock_response

            # Call the get_json function with the test URL
            result = get_json(test_url)

            # Assert that the mocked get method was called exactly once with the test URL as an argument
            mock_get.assert_called_once_with(test_url)

            # Assert that the output of get_json is equal to the test payload
            self.assertEqual(result, test_payload)