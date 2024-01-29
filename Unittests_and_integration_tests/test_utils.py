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
    def test_get_json(self, mock_requests_get):
        # Define test cases with test_url and corresponding test_payload
        test_cases = [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]

        # Iterate through test cases
        for test_url, test_payload in test_cases:
            # Mock the json method of the get result to return the test_payload
            mock_get_result = Mock()
            mock_get_result.json.return_value = test_payload
            mock_requests_get.return_value = mock_get_result

            # Call the get_json function with the test_url
            result = get_json(test_url)

            # Assert that requests.get was called exactly once with the correct argument
            mock_requests_get.assert_called_once_with(test_url)

            # Assert that the result of get_json is equal to the test_payload
            self.assertEqual(result, test_payload)

            # Reset the mock_calls