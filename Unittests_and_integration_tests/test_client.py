#!/usr/bin/env python3
"""This will be used to test the clientele
"""

import unittest
from unittest.mock import patch
from client import GithubOrgClient


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
        mock_get_json.assert_called_once_with
        (f'https://api.github.com/orgs/{org_name}')
        
        @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    def test_public_repos_url(self, org_name):
        """Test the _public_repos_url method of GithubOrgClient."""
        # Set up the expected result for the mock org property
        org_payload = {'organization': org_name}
        expected_public_repos_url = f'https://api.github.com/orgs/{org_name}/repos'

        # Use patch as a context manager to mock the org property
        with patch('client.GithubOrgClient.org', return_value=org_payload):
            # Create an instance of GithubOrgClient
            github_org_client = GithubOrgClient(org_name)

            # Call the _public_repos_url method
            result = github_org_client._public_repos_url()

            # Assertions
            self.assertEqual(result, expected_public_repos_url)
