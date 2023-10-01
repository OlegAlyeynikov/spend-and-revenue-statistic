from rest_framework import serializers
from .models import RevenueStatistic


class RevenueStatisticSerializer(serializers.ModelSerializer):
    total_revenue = serializers.DecimalField(max_digits=9, decimal_places=2)
    total_spend = serializers.DecimalField(max_digits=10, decimal_places=2)
    total_impressions = serializers.IntegerField()
    total_clicks = serializers.IntegerField()
    total_conversion = serializers.IntegerField()

    class Meta:
        model = RevenueStatistic
        fields = (
            'date', 'name', 'total_revenue', 'total_spend',
            'total_impressions', 'total_clicks', 'total_conversion')
