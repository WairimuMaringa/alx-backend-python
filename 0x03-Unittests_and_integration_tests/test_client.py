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
