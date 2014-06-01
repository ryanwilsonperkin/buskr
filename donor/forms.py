from django import forms

class CreditCardDonation(forms.Form):
    cardholder_name = models.CharField(max_length=100)
    expire_month = models.IntegerField()
    expire_year = models.IntegerField()
    cvv2 = models.IntegerField()
    amount = models.DecimalField(max_digits=5, decimal_places=2)
