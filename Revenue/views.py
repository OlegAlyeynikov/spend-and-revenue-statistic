from rest_framework import viewsets
from Revenue.models import RevenueStatistic
from Revenue.serializer import RevenueStatisticSerializer
from django.db.models import Sum


class RevenueViewSet(viewsets.ModelViewSet):
    queryset = RevenueStatistic.objects.all()
    serializer_class = RevenueStatisticSerializer

    def get_queryset(self):
        queryset = self.queryset.values('date', 'name').annotate(
            total_revenue=Sum('revenue'),
            total_spend=Sum('spend__spend'),
            total_impressions=Sum('spend__impressions'),
            total_clicks=Sum('spend__clicks'),
            total_conversion=Sum('spend__conversion')
        )
        return queryset
