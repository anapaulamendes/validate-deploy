from django.db import models


class Release(models.Model):
    ReleaseName = models.CharField(max_length=255)
    ReleaseId = models.IntegerField(unique=True)
    TeamProject = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.ReleaseName} - {self.ReleaseId} - {self.TeamProject}"


class Approvals(models.Model):
    token = models.CharField(max_length=255, unique=True)
    approved = models.BooleanField(default=False)
    email = models.EmailField(max_length=255, unique=True)
    release = models.ForeignKey(
        Release, null=True, on_delete=models.PROTECT, related_name="approvals"
    )

    def __str__(self):
        return f"{self.token} - {self.email} - {self.approved}"
