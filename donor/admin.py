from django.contrib import admin

from donor.models import CreditCard, Donation

admin.site.register(CreditCard)
admin.site.register(Donation)
