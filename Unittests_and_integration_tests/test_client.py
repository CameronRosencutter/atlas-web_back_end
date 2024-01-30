#!/usr/bin/env python3
"""This will be used to test the clientele
"""

import unittest
import fixtures
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, PropertyMock, Mock

class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient class."""

    @patch('client.GithubOrgClient.get_json')
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    def test_org(self, org_name, mock_get_json):
        """Test the org method of GithubOrgClient."""
        # Set up the expected result for the mock get_json call
        expected_result = {'organization': org_name}

        # Configure the mock get_json method
        mock_get_json.return_value = expected_result

        # Create an instance of GithubOrgClient
        github_org_client = GithubOrgClient(org_name)

        # Call the org method
        result = github_org_client.org()

        # Assertions
        self.assertEqual(result, expected_result)
        mock_get_json.assert_called_once_with(f'https://api.github.com/orgs/{org_name}')
