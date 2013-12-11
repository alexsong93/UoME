from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from UoMeApp.models import UoMePost, Group
from UoMeApp.views import myGroupsView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'UoMe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    #homepage
    url(r'^$','UoMeApp.views.homepage'),
    
    #facebook
    #url(r'^$', include('social_auth.urls')),
    
    # user auth urls
    url(r'^accounts/login/?$', 'UoMe.views.login'),
    url(r'^accounts/auth/?$', 'UoMe.views.auth_view'),
    url(r'^accounts/logout/?$', 'UoMe.views.logout'),
    url(r'^accounts/register/?$', 'UoMe.views.register_user'),
    
    # Dashboard
    url(r'^dashboard/?$', 'UoMeApp.views.loadDashboard'),
           
    # Profile
    url(r'^profile/?$', 'UoMeApp.views.profile'),
                       
    # All groups
    url(r'^groups/?$', myGroupsView.as_view(
        model=Group,
    )),
                       
    # Create a group
    url(r'^create/group/?$', 'UoMeApp.views.createGroup'),
                       
    # Add a UoMePost
    url(r'^addUoMe/(?P<group_id>\d)/?$', 'UoMeApp.views.addUoMePost'),
    # Edit a UoMePost
    url(r'^edit/(?P<group_id>\d)/(?P<uomepost_id>\d)/?$', 'UoMeApp.views.editUoMePost'),
    # notifications
    url(r'^notify/paid/(?P<uomepost_id>\d)/?$', 'UoMeApp.views.notifyPaid'),
    url(r'^notify/confirm/(?P<uomepost_id>\d)/?$', 'UoMeApp.views.notifyConfirm'),
    url(r'^notify/reject/(?P<uomepost_id>\d)/?$', 'UoMeApp.views.notifyReject'),
    
    # flatpages
    url(r'', include('django.contrib.flatpages.urls')),
#     url(r'^events/(?P<categorySlug>\w+)/?$', 'UoMeApp.views.getEvent'),
#     url(r'^events/(?P<categorySlug>\w+)/(?P<selected_page>\d+)/?$', 'UoMeApp.views.getEvent'),
)
