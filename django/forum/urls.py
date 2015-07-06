from django.conf.urls import patterns, url

urlpatterns = patterns('forum.views',
    url(r'^$', 'home'),
    url(r'^accueil$', 'home'),
    url(r'^posts/(?P<cat>\d+)$', 'list_posts'),
    url(r'^post/(?P<p>\d+)$', 'post'),
    url(r'^add$', 'add_post'),
    url(r'^add_msg/(?P<p>\d+)$', 'add_msg'),
    url(r'^msg_reply/(?P<p>\d+)$', 'msg_reply'),
)

