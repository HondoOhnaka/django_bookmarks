from django.http import HttpResponse
def main_page(request):
    output = u'''
    <html>
    <head><title>%s</title></head>
    <body>
    <h1>%s</h1><p>%s</p>
    </body>
    </html>
    ''' % (
    u'Django Bookmarks',
    u'Welcome to Django Bookmarks',
    u'Where you can store and share bookmarks!'
    )
    return HttpResponse(output)