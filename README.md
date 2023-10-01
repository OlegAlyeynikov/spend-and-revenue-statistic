# spend-and-revenue-statistic

## Тестове завдання
В проекте Django є 2 застосунки (apps) - spend та revenue

файл models.py в Spend має наступний вигляд:
class SpendStatistic(models.Model):
   name = models.CharField(max_length=255)
   date = models.DateField()
   spend = models.DecimalField(max_digits=10, decimal_places=2, default=0)
   impressions = models.IntegerField(default=0)
   clicks = models.IntegerField(default=0)
   conversion = models.IntegerField(default=0)

файл models.py в Revenue має наступний вигляд:
class RevenueStatistic(models.Model):
   name = models.CharField(max_length=255)
   spend = models.ForeignKey('spend.SpendStatistic',    on_delete=models.SET_NULL, null=True)
   date = models.DateField()
   revenue = models.DecimalField(max_digits=9, decimal_places=2,   default=0)


Завдання.

Написати файл views.py в revenue. Реалізувати ендпоинт в якому ми отримуємо queryset моделі RevenueStatistic 
з поділом по дням (date) та назвою (name), з агрегованими сумами значень revenue та пов'язаними 
значеннями spend, impressions, clicks, conversion з моделі SpendStatistic.

Написати файл views.py в spend. Реалізувати ендпоинт в якому ми отримуємо queryset моделі SpendStatistic 
з поділом по дням (date) та назвою (name), з агрегованими сумами значень spend, impressions, 
clicks, conversion та пов'язаними значеннями revenue з моделі RevenueStatistic.

Використовувати засоби Django Rest Framework.
serializers.py писати необов’язково.
Виконане завдання викласти на GitHub та переслати ссилку.
Уточнюючі питання з тестового завдання сюди - @developer_for
