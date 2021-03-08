from rest_framework import viewsets

from core.models import Approvals, Release
from core.serializers import ApprovalsSerializer, ReleaseSerializer


class ReleaseViewSet(viewsets.ModelViewSet):
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer


class ApprovalsViewSet(viewsets.ModelViewSet):
    queryset = Approvals.objects.all()
    serializer_class = ApprovalsSerializer
