from unittest.mock import Mock, patch

from faker import Faker
from rest_framework.test import APITestCase

from core.services.send_email import SendEmail


class SendEmailTest(APITestCase):
    def setUp(self):
        self.fake = Faker()
        self.to_emails = [self.fake.email(), self.fake.email()]
        self.subject = self.fake.text(max_nb_chars=80)
        self.message = self.fake.text(max_nb_chars=500)
        self.send_email_wrapper = SendEmail(self.to_emails, self.subject, self.message)

    @patch("sendgrid.base_interface.BaseInterface.send")
    def test_send_email(self, mock):
        mock.return_value = Mock(ok=True)
        mock.return_value.status_code = 202
        self.send_email_wrapper.send_email()
        mock.assert_called_once()

    @patch("sendgrid.base_interface.BaseInterface.send")
    def test_send_email_raise_exception(self, mock):
        mock.side_effect = Exception(
            "python_http_client.exceptions.ForbiddenError: HTTP Error 403: Forbidden"
        )
        with self.assertRaises(Exception):
            self.send_email_wrapper.send_email()
