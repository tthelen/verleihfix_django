from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings as django_settings
from django.contrib.auth.views import login, logout
from django.conf.urls.static import static
from Verleihfix.views import home, type, lend, lendings, lending_status, settings, about
from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    # Examples:
    # url(r'^$', 'verleihfix_tthelen_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', home, name='home' ),
    url(r'^type/(?P<type_id>\d+)$', type, name='type'),
    url(r'^lend$', lend, name='lend'),
    url(r'^lendings$', lendings, name='lendings'),
    url(r'^lending_status$', lending_status, name='lending_status'),
    url(r'^settings$', settings, name='settings'),
    url(r'^about$', about, name='about'),

    url(r'^accounts/login/?$', login, {'template_name': 'admin/login.html',
       'extra_context':{'next':'/'}}, name='login'),
    url(r'^accounts/logout/?$', logout, {'next_page': '/'}, name='logout'),
    url(r'^jsi18n/$', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    url(r'^i18n/', include('django.conf.urls.i18n'))

] + static(django_settings.MEDIA_URL, document_root=django_settings.MEDIA_ROOT)

