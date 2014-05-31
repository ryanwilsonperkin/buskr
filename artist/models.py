from django.db import models

class Artist(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    description = models.CharField(max_length=140)
    thank_you_message = models.CharField(max_length=140)
