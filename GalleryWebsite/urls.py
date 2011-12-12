from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from GalleryWebsite import settings
from profiles.views import *
from django.contrib.auth.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       
                       
    (r'^accounts/', include('registration.backends.default.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^profile/$',profile_detail),
    (r'^profile/create/$',profile_create),
    (r'^profile/edit/$',profile_edit),
    (r'^$',profile_detail),
    (r'^mmedia/(?P<path>.*)$', 'django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
)
