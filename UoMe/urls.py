from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from UoMeApp.models import Event, UoMePost, Group

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'UoMe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    # user auth urls
    url(r'^accounts/login/?$', 'UoMe.views.login'),
    url(r'^accounts/auth/?$', 'UoMe.views.auth_view'),
    url(r'^accounts/logout/?$', 'UoMe.views.logout'),
    url(r'^accounts/loggedin/?$', 'UoMe.views.loggedin'),
    url(r'^accounts/invalid/?$', 'UoMe.views.invalid_login'),
    url(r'^accounts/register/?$', 'UoMe.views.register_user'),
    url(r'^accounts/register_success/?$', 'UoMe.views.register_success'),
    
    # Dashboard
    url(r'^dashboard/?$', 'UoMeApp.views.createDashboard'),
    # Events
    url(r'^events/?$', ListView.as_view(
        model=Event,
    )),
                       
    # All groups
    url(r'^groups/?$', ListView.as_view(
        model=Group,
    )),
                       
    # All posts
    url(r'^UoMePosts/?$', ListView.as_view(
        model=UoMePost,
    )),
                       
    # Create a group
    url(r'^create/group/?$', 'UoMeApp.views.createGroup'),
                       
    # Add a UoMePost
    url(r'^create/?$', 'UoMeApp.views.create'),

    # flatpages
    url(r'', include('django.contrib.flatpages.urls')),
#     url(r'^events/(?P<categorySlug>\w+)/?$', 'UoMeApp.views.getEvent'),
#     url(r'^events/(?P<categorySlug>\w+)/(?P<selected_page>\d+)/?$', 'UoMeApp.views.getEvent'),
)
