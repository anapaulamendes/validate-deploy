from django.urls import reverse
from rest_framework.test import APITestCase

from core.tests.factories.approvals import ApprovalsFactory
from core.tests.factories.release import ReleaseFactory


class ApprovalsViewSetTest(APITestCase):
    def setUp(self):
        self.release = ReleaseFactory()
        self.approval = ApprovalsFactory(approved=False, release=self.release)

    def test_approval_get_by_token(self):
        url = reverse("approval-list") + f"?token={self.approval.token}"
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
