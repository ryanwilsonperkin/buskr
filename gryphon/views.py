from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from artist.forms import CreateArtistForm
from artist.models import Artist
from donor.forms import CreditCardDonationForm
from donor.models import CreditCard, Donation
from donor.utils import make_credit_card_payment

def donate(request, id):
    try:
        id = int(id)
        artist = Artist.objects.get(pk=id)
    except (ValueError, ObjectDoesNotExist):
        artist = {} 
    if request.method == 'POST':
        form = CreditCardDonationForm(request.POST)
        if form.is_valid():
            cardholder_name = form.cleaned_data['cardholder_name']
            number = form.cleaned_data['number']
            expire_month = form.cleaned_data['expire_month']
            expire_year = form.cleaned_data['expire_year']
            cvv2 = form.cleaned_data['cvv2']
            amount = form.cleaned_data['amount']
            success = make_credit_card_payment(
                cardholder_name,
                number,
                expire_month,
                expire_year,
                cvv2,
                amount
            )
            if success:
                return HttpResponseRedirect('/thanks/')
            else:
                return HttpResponseRedirect('/damn/')
    else:
        form = CreditCardDonationForm()
    return render(request, 'donate.html', {
        'artist': artist,
        'form': form,
    })

def landing_page(request):
    return render(request, 'landing_page.html')

def profile(request):
    if request.method == 'POST':
        form = CreateArtistForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            profession = form.cleaned_data['profession']
            description = form.cleaned_data['description']
            thank_you_message = form.cleaned_data['thank_you_message']
            return HttpResponseRedirect('/share/')
    else:
        form = CreateArtistForm()

    return render(request, 'profile.html', {
        'form': form,
    })

def share(request, id):
    try:
        id = int(id)
        artist = Artist.objects.get(pk=id)
    except (ValueError, ObjectDoesNotExist):
        artist = {}
    return render(request, 'share.html', {'artist': artist})
