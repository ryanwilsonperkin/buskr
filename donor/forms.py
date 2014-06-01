from django import forms

class CreditCardDonationForm(forms.Form):
    cardholder_name = forms.CharField(max_length=100)
    number = forms.BigIntegerField()
    expire_month = forms.IntegerField()
    expire_year = forms.IntegerField()
    cvv2 = forms.IntegerField()
    amount = forms.DecimalField(max_digits=5, decimal_places=2)
