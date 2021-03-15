from rest_framework import filters, serializers

from core.models import Approvals, Release


class ReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Release
        fields = "__all__"


class ApprovalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Approvals
        fields = (
            "token",
            "approved",
            "email",
        )
        read_only_fields = ("release",)
        filter_backends = (filters.SearchFilter,)
        search_fields = ("token",)
