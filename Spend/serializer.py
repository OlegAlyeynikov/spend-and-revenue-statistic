from rest_framework import serializers
from Spend.models import SpendStatistic


class SpendStatisticSerializer(serializers.ModelSerializer):
    date = serializers.DateField()
    name = serializers.CharField(max_length=255)
    total_spend = serializers.DecimalField(max_digits=10, decimal_places=2)
    total_impressions = serializers.IntegerField()
    total_clicks = serializers.IntegerField()
    total_conversion = serializers.IntegerField()
    total_revenue = serializers.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        model = SpendStatistic
        fields = ("id", "name", "date", "total_spend", "total_impressions",
                  "total_clicks", "total_conversion", "total_revenue")
