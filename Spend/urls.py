from django.urls import path, include
from rest_framework import routers

# from station.views import BusViewSet, TripViewSet, FacilityViewSet, OrderViewSet, TicketViewSet

router = routers.DefaultRouter()
# router.register("facilities", FacilityViewSet)
# router.register("buses", BusViewSet)
# router.register("trips", TripViewSet)
# router.register("orders", OrderViewSet)
# router.register("tickets", TicketViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "Spend"
