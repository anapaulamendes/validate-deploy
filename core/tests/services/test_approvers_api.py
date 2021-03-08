from unittest.mock import Mock, patch

from faker import Faker
from rest_framework.test import APITestCase

from core.services.approvers_api import ApproversAPI


class ApproversAPITest(APITestCase):
    def setUp(self):
        self.fake = Faker()
        self.approvers_api_wrapper = ApproversAPI()
        self.json = {"approvers": [self.fake.email(), self.fake.email()]}

    @patch("requests.sessions.Session.get")
    def test_get_approvers(self, mock):
        mock.return_value = Mock(ok=True)
        mock.return_value.json.return_value = self.json
        mock.return_value.status_code = 200
        resp = self.approvers_api_wrapper.get_approvers()
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json(), self.json)

    @patch("requests.sessions.Session.get")
    def test_get_approvers_raise_exception(self, mock):
        mock.side_effect = Exception()
        with self.assertRaises(Exception):
            self.approvers_api_wrapper.get_approvers()
