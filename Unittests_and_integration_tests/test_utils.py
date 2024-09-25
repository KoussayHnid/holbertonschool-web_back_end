#!/usr/bin/env python3
"""
Parameterize a unit test
"""
from unittest import TestCase, mock
from parameterized import parameterized, parameterized_class  # type: ignore
from utils import access_nested_map, get_json  # type: ignore
from unittest.mock import Mock, patch, PropertyMock
from client import GithubOrgClient  # type: ignore
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos  # type: ignore


class TestAccessNestedMap(TestCase):
    """
    Class that inherits from unittest.TestCase
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected_output):
        """
        Test that the method returns the correct output.
        """
        output = access_nested_map(map, path)
        self.assertEqual(output, expected_output)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, map, path, ErrMessage):
        """
        Test that the method raises a KeyError.
        """
        with self.assertRaises(KeyError) as er:
            access_nested_map(map, path)
        self.assertEqual(str(er.exception), f"'{ErrMessage}'")


class TestGetJson(TestCase):
    """
    Mock HTTP calls
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Test that function returns the expected result.
        """
        mock_returned = Mock()
        mock_returned.json.return_value = test_payload
        with patch('requests.get', return_value=mock_returned):
            test_response = get_json(test_url)
            self.assertEqual(test_response, test_payload)
            mock_returned.json.assert_called_once()

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """
        Test that _public_repos_url returns the correct URL.
        """
        mock_org.return_value = {"repos_url": "https://api.github.com/orgs/google/repos"}
        client = GithubOrgClient("google")
        self.assertEqual(client._public_repos_url, mock_org.return_value["repos_url"])

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """
        Test GithubOrgClient.public_repos.
        """
        mock_public_repos_url.return_value = "https://api.github.com/orgs/google/repos"
        mock_get_json.return_value = [{"name": "repo1"}, {"name": "repo2"}]
        client = GithubOrgClient("google")
        repos = client.public_repos()
        self.assertEqual(repos, ["repo1", "repo2"])
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with("https://api.github.com/orgs/google/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test GithubOrgClient.has_license.
        """
        client = GithubOrgClient("google")
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class(('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'), [  # type: ignore
    (org_payload, repos_payload, expected_repos, apache2_repos)
])
class TestIntegrationGithubOrgClient(TestCase):
    """
    Integration tests for GithubOrgClient
    """

    @classmethod
    def setUpClass(cls):
        """
        Start patching requests.get
        """
        cls.get_patcher = patch('requests.get')
        mock_get = cls.get_patcher.start()

        # Mocking requests.get().json() to return different fixtures
        mock_get.return_value.json.side_effect = [
            cls.org_payload, cls.repos_payload
        ]

    @classmethod
    def tearDownClass(cls):
        """
        Stop patching requests.get
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Test public_repos method
        """
        client = GithubOrgClient("google")
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """
        Test public_repos with license='apache-2.0'
        """
        client = GithubOrgClient("google")
        repos = client.public_repos(license="apache-2.0")
        self.assertEqual(repos, self.apache2_repos)

    # Task 8: Add tests for organization public repos using integration test
    def test_integration_public_repos(self):
        """
        Test the integration with the organization public repos.
        """
        client = GithubOrgClient("google")
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    # Task 9: Add a test for organization public repos with a specific license
    def test_integration_public_repos_with_license(self):
        """
        Test public_repos with license='apache-2.0' during integration.
        """
        client = GithubOrgClient("google")
        repos = client.public_repos(license="apache-2.0")
        self.assertEqual(repos, self.apache2_repos)
