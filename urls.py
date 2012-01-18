from django.conf.urls.defaults import *
from bookmarks.views import *
from django.views.generic.simple import direct_to_template
import os
from django.contrib import admin
from bookmarks.feeds import *

admin.autodiscover()

site_media = os.path.join(
    os.path.dirname(__file__), 'site_media'
    )
    
# Add the feeds dict before the urlpattern object

feeds = { 'recent': RecentBookmarks, 'user': UserBookmarks }

urlpatterns = patterns('', 
    #browsing
    (r'^$', main_page),
	(r'^popular/$', popular_page),
    (r'^user/(\w+)/$', user_page),
    (r'^tag/([^\s]+)/$', tag_page),
    (r'^tag/$', tag_cloud_page),
	(r'^search/$', search_page),
	(r'^bookmark/(\d+)/$', bookmark_page),
	
	#friends 
	(r'^friends/(\w+)/$', friends_page),
	(r'^friend/add/$', friend_add),
	
	# Admin interface (chap 8)
	# (r'^admin/(.*)', admin.site.root),
	# fixed via         stackoverflow.com/questions/5503616/how-to-correct-this-error-adminsite-object-has-no-attribute-root
	url(r'^admin/', include(admin.site.urls)),
		
	#Ajax
	(r'^ajax/tag/autocomplete/$', ajax_tag_autocomplete),
    
    #session management
    (r'^login/$',
        'django.contrib.auth.views.login'),
    (r'^logout/$', logout_page),
    
    (r'^register/$', register_page),
    (r'register/success/$', direct_to_template,
        {'template': 'registration/register_success.html'}),
    
    #account management
    (r'^save/$', bookmark_save_page),
    (r'^vote/$', bookmark_vote_page),
    
    #site media
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': site_media}),

	# comments (chap 7)
	(r'^comments/', include('django.contrib.comments.urls')),
	
	# feeds (chapter 9)
	(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', 
	    {'feed_dict': feeds}),
    
)
