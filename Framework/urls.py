from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Framework.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'', include('intra.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^forum/', include('forum.urls')),
    url(r'^ticket/', include('ticket.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
