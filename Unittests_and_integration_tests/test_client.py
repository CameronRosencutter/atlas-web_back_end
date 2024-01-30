#!/usr/bin/env python3
"""This will be used to test the clientele
"""

import unittest
import requests
from unittest.mock import (
    patch,
    PropertyMock,
    MagicMock
)
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD


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

    def test_public_repos(self, org_name, mock_public_repos_url, mock_get_json):
        """Test the public_repos method of GithubOrgClient."""
        # Set up the expected result for the mock _public_repos_url
        expected_public_repos_url = f'https://api.github.com/orgs/{org_name}/repos'

        # Set up the expected payload for the mock get_json
        expected_payload = [{'repo1': 'details1'}, {'repo2': 'details2'}]

        # Configure the mock _public_repos_url return value
        mock_public_repos_url.return_value = expected_public_repos_url

        # Configure the mock get_json return value
        mock_get_json.return_value = expected_payload

        # Create an instance of GithubOrgClient
        github_org_client = GithubOrgClient(org_name)

        # Call the public_repos method
        result = github_org_client.public_repos()

        # Assertions
        self.assertEqual(result, expected_payload)
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with(expected_public_repos_url)

class TestGithubOrgClient:
    @pytest.mark.parametrize("repo, license_key, expected", [
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        # Create an instance of your GithubOrgClient class
        github_client = GithubOrgClient()

        # Call the has_license method with the provided parameters
        result = github_client.has_license(repo, license_key)

        # Check if the result matches the expected value
        assert result == expected