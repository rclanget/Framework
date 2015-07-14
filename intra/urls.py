from django.conf.urls import patterns, url

urlpatterns = patterns('intra.views',
    url(r'^$', 'home'),
    url(r'^accueil$', 'home'),
    url(r'^contact$', 'contact'),
    url(r'^user_register$', 'user_register'),
    url(r'^user_login$', 'user_login'),
    url(r'^user_logout$', 'user_logout'),
    url(r'^test$', 'test'),
)
