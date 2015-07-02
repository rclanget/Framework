from django.conf.urls import patterns, url

urlpatterns = patterns('intra.views',
    url(r'^$', 'home'),
    url(r'^accueil$', 'home'),
)
