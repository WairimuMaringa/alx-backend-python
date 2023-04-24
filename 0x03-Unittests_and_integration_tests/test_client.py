#!/usr/bin/env python3
"""
Client tests
"""
import unittest
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from unittest.mock import patch, Mock, PropertyMock
from fixtures import TEST_PAYLOAD
import json


class TestGithubOrgClient(unittest.TestCase):
    """ Tests the github org client. """

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, orgname, mock):
        """ Tests for correct output. """
        test_class = GithubOrgClient(orgname)
        test_class.org()
        mock.assert_called_once_with(f'https://api.github.com/orgs/{orgname}')

    def test_public_repos_url(self):
        """ Tests for correct output. """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            payload = {"repos_url": "World"}
            mock.return_value = payload
            test_class = GithubOrgClient('test')
            result = test_class._public_repos_url
            self.assertEqual(result, payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """ Tests for expected repos. """
        json_payload = [{"name": "Google"}, {"name": "Twitter"}]
        mock_json.return_value = json_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public:
            mock_public.return_value = "hello/world"
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()

            check = [i["name"] for i in json_payload]
            self.assertEqual(result, check)

            mock_public.assert_called_once()
            mock_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "react2"}}, "react", False),
        ({"license": {"key": "django"}}, "django", True)
        ])
    def test_has_license(self, repo, license, expected):
        """ Test for license. """
        test_class = GithubOrgClient('django')
        return_value = test_class.has_license(repo, license)
        self.assertEqual(return_value, expected)


@parameterized_class(
        ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
        TEST_PAYLOAD
        )
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Test for github org client. """

    @classmethod
    def setUpClass(cls):
        """ set class. """
        cls.get_patcher = patch('requests.get', side_effect=HTTPError)

    @parameterized.expand([
        ({"license": {"key": "react2"}}, "react", False),
        ({"license": {"key": "django"}}, "django", True)
        ])
    def test_has_license(self, repo, license, expected):
        """ Test for license that is expected. """
        test_class = GithubOrgClient('django')
        return_value = test_class.has_license(repo, license)
        self.assertEqual(return_value, expected)

    @classmethod
    def tearDownClass(cls)
    """ tear down the class. """
    cls.get_patcher.stop()
