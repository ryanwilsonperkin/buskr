from django import forms

class CreateArtistForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    profession = forms.CharField(max_length=100)
    description = forms.CharField(max_length=140)
    thank_you_message = forms.CharField(max_length=140)
