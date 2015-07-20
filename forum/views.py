#-*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from forum.models import PostCategorie, PostSsCategorie, Post, PostMessage, Thread
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.utils.translation import ugettext as _

def home(request):
    if request.user.is_authenticated():
        categories = PostCategorie.objects.all()
        sscategories = PostSsCategorie.objects.all()
        posts = Post.objects.order_by('-date')[:5]
        return render(request, 'forum/index.html', locals())
    else:
        return render(request, 'intra/index.html')

def list_posts(request, cat):
    if request.user.is_authenticated():
        categories = PostCategorie.objects.all()
        sscategories = PostSsCategorie.objects.all()
        mycat = PostCategorie.objects.get(id=cat)
        posts = Post.objects.filter(categorie=cat).order_by('-date')
        return render(request, 'forum/list_posts.html', locals())
    else:
        return render(request, 'intra/index.html')

def post(request, p):
    if request.user.is_authenticated():
        categories = PostCategorie.objects.all()
        sscategories = PostSsCategorie.objects.all()
        post = Post.objects.get(id=p)
        msgs = PostMessage.objects.filter(post=p)
        thread = Thread.objects.all()
        return render(request, 'forum/post.html', locals())
    else:
        return render(request, 'intra/index.html')

def list_posts_bysscat(request, cat, sscat):
    if request.user.is_authenticated():
        categories = PostCategorie.objects.all()
        sscategories = PostSsCategorie.objects.all()
        mycat = PostCategorie.objects.get(id=cat)
        mysscat = PostSsCategorie.objects.get(id=sscat)
        posts = Post.objects.filter(sscategorie=sscat).order_by('-date')
        return render(request, 'forum/list_posts.html', locals())
    else:
        return render(request, 'intra/index.html')

def add_post(request):
    if request.user.is_authenticated():
        categories = PostCategorie.objects.all()
        sscategories = PostSsCategorie.objects.all()
        cats = PostCategorie.objects.all()
        sscats = PostSsCategorie.objects.all()
        if request.method == 'POST':
            if request.POST['titre'] and request.POST['message']:
                if request.POST["sscategorie"] == "null":
                    sscat = None
                else:
                    sscat = PostSsCategorie.objects.get(name=request.POST["sscategorie"])
                cat = PostCategorie.objects.get(name=request.POST['categorie'])
                Post(titre=request.POST['titre'], auteur=request.user.username, sscategorie=sscat, categorie=cat).save()
                if Post.objects.filter(titre=request.POST['titre']).count() > 1:
                    messages.add_message(request, messages.ERROR, _("Titre existant !"))
                    return render(request, 'forum/new.html', locals())
                mypost = Post.objects.get(titre=request.POST['titre'])
                PostMessage(content=request.POST['message'], auteur=request.user.username, post=mypost).save()
                messages.add_message(request, messages.SUCCESS, _("Post ajoute"))
            else:
                messages.add_message(request, messages.ERROR, _("Formulaire incomplet !"))
        return render(request, 'forum/new.html', locals())
    return render(request, 'intra/index.html')

def add_msg(request, p):
    mypost = Post.objects.get(id=request.POST['id'])
    PostMessage(content=request.POST['message'], auteur=request.user.username, post=mypost).save()
    return HttpResponseRedirect(reverse('forum.views.post', kwargs={'p': p}))

def msg_reply(request, p):
    mypost = Post.objects.get(id=request.POST['id'])
    mymsg = PostMessage.objects.get(id=request.POST['msg_id'])
    Thread(content=request.POST['message'], auteur=request.user.username, postmessage=mymsg).save()
    return HttpResponseRedirect(reverse('forum.views.post', kwargs={'p': p}))
