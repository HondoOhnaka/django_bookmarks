from django.conf.urls.defaults import *
from bookmarks.views import *
from django.views.generic.simple import direct_to_template
import os

site_media = os.path.join(
    os.path.dirname(__file__), 'site_media'
    )

urlpatterns = patterns('', 
    #browsing
    (r'^$', main_page),
    (r'^user/(\w+)/$', user_page),
    (r'^tag/([^\s]+)/$', tag_page),
    (r'^tag/$', tag_cloud_page),
    
    #session management
    (r'^login/$',
        'django.contrib.auth.views.login'),
    (r'^logout/$', logout_page),
    
    (r'^register/$', register_page),
    (r'register/success/$', direct_to_template,
        {'template': 'registration/register_success.html'}),
    
    #account management
    (r'^save/$', bookmark_save_page),
    
    #site media
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': site_media}),
    
)
