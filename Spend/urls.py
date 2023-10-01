from django.urls import path, include
from rest_framework import routers

from Spend.views import SpendViewSet

router = routers.DefaultRouter()
router.register("spend", SpendViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "Spend"
