from django.urls import path, include
from rest_framework import routers
from Revenue.views import RevenueViewSet

router = routers.DefaultRouter()
router.register("revenue", RevenueViewSet)

urlpatterns = [
    path("", include(router.urls))
]

app_name = "Revenue"
