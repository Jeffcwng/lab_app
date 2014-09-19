from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.templatetags.static import static
from lab_app import settings
from wanderful.models import Location


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lab_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'wanderful.views.home', name='home'),
    url(r'^testing/$', 'wanderful.views.testing', name='testing'),
    url(r'^testing3/$', 'wanderful.views.testing3', name='testing3'),
    url(r'^profile/$', 'wanderful.views.profile', name='profile'),

    #map
    url(r'^map/$', 'wanderful.views.map', name='map'),

    #travel
    url(r'^traveler/$', 'wanderful.views.traveler', name='traveler'),
    url(r'^traveler/new/$', 'wanderful.views.new_traveler', name='new_traveler'),
    url(r'^traveler/(?P<traveler_id>\w+)/$', 'wanderful.views.view_traveler', name='view_traveler'),


     #location
    url(r'^location/$', 'wanderful.views.location', name='location'),
    url(r'^location/new/$', 'wanderful.views.new_location', name='new_location'),
    url(r'^location/(?P<location_id>\w+)/$', 'wanderful.views.view_location', name='view_location'),

    #travel list
    url(r'^travellist/$', 'wanderful.views.travellist', name='travellist'),
    url(r'^travellist/new/$', 'wanderful.views.new_travellist', name='new_travellist'),
    url(r'^travellist/(?P<travellist_id>\w+)/$', 'wanderful.views.view_travellist', name='view_travellist'),

    # register log in and out
    url(r'^register/$', 'wanderful.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),

    #password reset
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),

)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
