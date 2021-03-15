from unittest.mock import Mock, patch

from django.test import TestCase

from core.models import Approvals, Release
from core.serializers import ReleaseSerializer


class ReleaseSerializerTest(TestCase):
    def setUp(self):
        self.data = {
            "ReleaseName": "Teste Name",
            "ReleaseId": 1,
            "TeamProject": "Test Team",
        }

    @patch("core.services.approvers_api.ApproversAPI.get_approvers")
    def test_valid_data(self, mock):
        mock.return_value = Mock(ok=True)
        mock.return_value.status_code = 200
        mock.return_value.json.return_value = {
            "approvers": ["anapaula.ds.mendes@gmail.com"]
        }
        serializer = ReleaseSerializer(data=self.data)
        self.assertTrue(serializer.is_valid())
        serializer.save()
        self.assertEqual(1, Release.objects.count())
        self.assertEqual(1, Approvals.objects.count())
