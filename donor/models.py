from django.db import models

class CreditCard(models.Model):
    cardholder_name = models.CharField(max_length=100)
    number = models.BigIntegerField()
    expire_month = models.IntegerField()
    expire_year = models.IntegerField()
    cvv2 = models.IntegerField()

class Donation(models.Model):
    credit_card = models.ForeignKey(CreditCard)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    currency = models.CharField(max_length=5)
    description = models.CharField(max_length=140)
