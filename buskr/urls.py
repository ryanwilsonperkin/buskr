from django.conf.urls import patterns, include, url
from django.contrib import admin

from buskr.views import donate, landing_page, profile, share, thankyou
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^/?$', landing_page),
    url(r'^donate/(\d*)/?$', donate),
    url(r'^share/(\d*)/?$', share),
    url(r'^profile/?$', profile),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^thankyou/', thankyou),
)
