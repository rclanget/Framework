from django.conf.urls import patterns, url

urlpatterns = patterns('forum.views',
    url(r'^$', 'home'),
    url(r'^accueil$', 'home'),
                       url(r'^posts/(?P<categorie>\d+)/(?P<sscategorie>\d+)$', 'list_posts_bysscat'),
    url(r'^posts/(?P<categorie>\d+)$', 'list_posts'),
    url(r'^add$', 'add_post'),
)

