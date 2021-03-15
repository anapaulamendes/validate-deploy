import uuid

from django.urls import reverse
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from core.models import Approvals, Release
from core.services.approvers_api import ApproversAPI
from core.services.send_email import SendEmail


class ValidateDeploy:
    def __init__(self, validated_data):
        self.validated_data = validated_data
        self.approvers_api_wrapper = ApproversAPI()

    def validate(self):
        release_id = self.validated_data["ReleaseId"]
        query = Release.objects.filter(ReleaseId=release_id)
        if query.exists():
            release_object = query.first()
            status = (
                False
                if release_object.approvals.filter(approved=False).exists()
                else True
            )
            return Response({"status": {"approved": status}}, status=HTTP_200_OK)
        else:
            release_object = Release.objects.create(**self.validated_data)
            resp = self.approvers_api_wrapper.get_approvers()
            approvers = resp.json()["approvers"]
            for approver in approvers:
                approval_obj = Approvals.objects.create(
                    token=uuid.uuid4(), email=approver
                )
                release_object.approvals.add(approval_obj)
                url = reverse("approval-detail", kwargs={"pk": approval_obj.pk})
                homepage = "http://127.0.0.1:8000"
                subject = "Approve Deploy"
                content = f"<p><strong>Your token</strong>:&nbsp;{approval_obj.token}</p> \
                            <p><strong>URL to approve the deploy</strong>:&nbsp;{homepage}{url}</p> \
                            <p><strong>Release Name</strong>:&nbsp;{release_object.ReleaseName}</p> \
                            <p><strong>Release Id</strong>:&nbsp;{release_object.ReleaseId}</p> \
                            <p><strong>Team Project</strong>:&nbsp;{release_object.TeamProject}</p>"
                self.send_email_wrapper = SendEmail(approver, subject, content)
                self.send_email_wrapper.send_email()
            return release_object
