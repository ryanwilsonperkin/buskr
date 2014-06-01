from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from artist.forms import CreateArtistForm
from artist.models import Artist

def donate(request, id):
    try:
        id = int(id)
        artist = Artist.objects.get(pk=id)
    except (ValueError, ObjectDoesNotExist):
        artist = {} 
    return render(request, 'donate.html', {'artist': artist})

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
            return HttpResponseRedirect('/thanks/')
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
