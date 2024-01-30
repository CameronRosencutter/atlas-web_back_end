#!/usr/bin/env python3
"""This will be used to test utilities.
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize

class TestAccessNestedMap(unittest.TestCase):
    """ TestAccessNestedMap class """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """access_nested_map test method, checks for expected result"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        ({}, ("a",), "Key 'a' not found in nested map"),
        ({"a": 1}, ("a", "b"), "Key 'b' not found in nested map"),
    ])
    def test_access_nested_map_exception(
            self, nested_map, path, expected_exception_message):
        """checks if method raises the correct exception"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)