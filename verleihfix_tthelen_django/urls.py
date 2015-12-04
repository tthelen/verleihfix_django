from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.views import login, logout
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'verleihfix_tthelen_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'Verleihfix.views.home', name='home' ),
    url(r'^lend$', 'Verleihfix.views.lend', name='lend'),
    url(r'^lendings$', 'Verleihfix.views.lendings', name='lendings'),
    url(r'^lending_status$', 'Verleihfix.views.lending_status', name='lending_status'),
    url(r'^settings$', 'Verleihfix.views.settings', name='settings'),
    url(r'^accounts/login/?$', login, {'template_name': 'admin/login.html',
       'extra_context':{'next':'/'}}, name='login'),
    url(r'^accounts/logout/?$', logout, {'next_page': '/'})

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
