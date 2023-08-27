from django.db import models

# Create your models here.
class Subscriber(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    Technology = models.CharField(max_length=50)

    class Payment(models.Model):
        first_name = models.CharField(max_length=50)
        last_name = models.CharField(max_length=50)
        email = models.EmailField(max_length=50)
        amount = models.CharField(max_length=50)

    class Meta:
        db_table = 'Subscriber'

    class Meta1:
        db_table = 'Payment'