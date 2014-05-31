from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render

from artist.models import Artist

def donate(request, id):
    try:
        id = int(id)
        artist = Artist.objects.get(pk=id)
    except (ValueError, ObjectDoesNotExist):
        raise Http404("Artist \"{}\" not found.".format(id))
    return render(request, 'donate.html', {'artist': artist})

def landing_page(request):
    return render(request, 'landing_page.html')

def profile(request):
    return render(request, 'profile.html')

def share(request, id):
    try:
        id = int(id)
        artist = Artist.objects.get(pk=id)
    except (ValueError, ObjectDoesNotExist):
        raise Http404("Artist \"{}\" not found.".format(id))
    return render(request, 'share.html', {'artist': artist})
