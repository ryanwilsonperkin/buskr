from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from artist.forms import CreateArtistForm
from artist.models import Artist
from donor.forms import CreditCardDonationForm
from donor.models import CreditCard, Donation
from donor.utils import make_donation

def donate(request, id):
    try:
        id = int(id)
        artist = Artist.objects.get(pk=id)
    except (ValueError, ObjectDoesNotExist):
        raise Http404()
    if request.method == 'POST':
        form = CreditCardDonationForm(request.POST)
        if form.is_valid():
            new_card = CreditCard(
                cardholder_name=form.cleaned_data['cardholder_name'],
                number=form.cleaned_data['number'],
                expire_month=form.cleaned_data['expire_month'],
                expire_year=form.cleaned_data['expire_year'],
                cvv2=form.cleaned_data['cvv2']
            )
            new_card.save()
            new_donation = Donation(
                card=new_card,
                amount=form.cleaned_data['amount'],
                currency='CAD',
                description='Donation through buskr.ca.',
                recipient=artist
            )
            new_donation.save()
            success = make_donation(new_donation)
            if success:
                return HttpResponseRedirect('/thankyou/')
            else:
                # Temporary workaround while PayPal api sends 500 errors
                return HttpResponseRedirect('/')
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
            new_artist = Artist(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                profession=form.cleaned_data['profession'],
                description=form.cleaned_data['description'],
                thank_you_message=form.cleaned_data['thank_you_message']
            )
            new_artist.save()
            return HttpResponseRedirect('/share/{id}'.format(id=new_artist.id))
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
        raise Http404()
    return render(request, 'share.html', {'artist': artist})

def thankyou(request):
    return render(request, 'thankyou.html')
