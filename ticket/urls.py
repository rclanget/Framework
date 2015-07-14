from django.conf.urls import patterns, url

urlpatterns = patterns('ticket.views',
    url(r'^$', 'home'),
    url(r'^accueil$', 'home'),
    url(r'^add$', 'add'),
    url(r'^new$', 'new_ticket'),
    url(r'^attribute$', 'attributeto'),
    url(r'^openorclose$', 'openorclose'),
    url(r'^reply$', 'reply'),
    url(r'^ticket/(?P<t>\d+)$', 'ticket'),
)
