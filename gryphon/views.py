from django.shortcuts import render

def donate(request, id):
    return render(request, 'donate.html', {'id': id})

def landing_page(request):
    return render(request, 'landing_page.html')

def profile(request):
    return render(request, 'profile.html')

def share(request, id):
    return render(request, 'share.html', {'id': id})
