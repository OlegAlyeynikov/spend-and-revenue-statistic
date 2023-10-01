from rest_framework import viewsets
from django.db.models import Sum
from Spend.models import SpendStatistic
from Spend.serializer import SpendStatisticSerializer


class SpendViewSet(viewsets.ModelViewSet):
    serializer_class = SpendStatisticSerializer
    queryset = SpendStatistic.objects.all()

    def get_queryset(self):
        queryset = SpendStatistic.objects.all().values('date', 'name').annotate(
            total_spend=Sum('spend'),
            total_impressions=Sum('impressions'),
            total_clicks=Sum('clicks'),
            total_conversion=Sum('conversion'),
            total_revenue=Sum('revenuestatistic__revenue')
        )
        return queryset
