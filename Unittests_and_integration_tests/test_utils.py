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
    def test_get_json(self,
                      url: str, payload: Dict[str, bool],
                      mock_requests: MagicMock
                      ) -> None:
        """This is defining the testgetjson option"""
        mock_requests.return_value.json.return_value = payload
        result = get_json(url)
        self.assertEqual(result, payload)

class TestMemoize(unittest.TestCase):
    """this is the testmemoize class"""

    def test_memoize(self):
        """ This is the testmemomize function"""

        class TestClass:
            """This is just testing everything out"""
            def __init__(self):
                """ init method"""
                self.call_count = 0

            def a_method(self):
                """method method method method"""
                self.call_count += 1
                return 42

            @memoize
            def a_property(self):
                """this is a property"""
                return self.a_method()
