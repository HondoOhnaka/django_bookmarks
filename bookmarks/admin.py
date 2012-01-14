from django.contrib import admin
from bookmarks.models import *

class LinkAdmin(admin.ModelAdmin):
    pass

class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'user')
    list_filter = ('title', 'user')
    ordering = ('user',)
    search_fields = ('title',)
    
class TagAdmin(admin.ModelAdmin):
    pass

class SharedBookmarkAdmin(admin.ModelAdmin):
    pass
        

admin.site.register(Link, LinkAdmin)
admin.site.register(Bookmark, BookmarkAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(SharedBookmark, SharedBookmarkAdmin)