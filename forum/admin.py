from django.contrib import admin
from forum.models import PostCategorie, PostSsCategorie, Post, PostMessage, Thread

admin.site.register(PostCategorie)
admin.site.register(PostSsCategorie)
admin.site.register(Post)
admin.site.register(PostMessage)
admin.site.register(Thread)
