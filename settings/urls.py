from rest_framework import routers

from core.views import ApprovalsViewSet, ReleaseViewSet

router = routers.SimpleRouter()
router.register(r"release", ReleaseViewSet, basename="release")
router.register(r"approval", ApprovalsViewSet, basename="approval")
urlpatterns = router.urls
