from django.conf.urls import patterns, include, url
from django.contrib import admin

from gryphon.views import donate, landing_page, profile, share
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', landing_page),
    url(r'^donate/(.*)$', donate),
    url(r'^share/(.*)$', share),
    url(r'^profile$', profile),
)
