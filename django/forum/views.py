#-*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from forum.models import PostCategorie, PostSsCategorie, Post, PostMessage, Thread
from django.core.urlresolvers import reverse

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
        mycat = PostSsCategorie.objects.get(id=cat)
        posts = Post.objects.filter(categorie=cat).order_by('-date')
        return render(request, 'forum/list_posts.html', locals())
    else:
        return render(request, 'intra/index.html')

def post(request, p):
    if request.user.is_authenticated():
        categories = PostCategorie.objects.all()
        sscategories = PostSsCategorie.objects.all()
        post = Post.objects.get(id=p)
        message = PostMessage.objects.filter(post=p)
        thread = Thread.objects.all()
        return render(request, 'forum/post.html', locals())
    else:
        return render(request, 'intra/index.html')

def list_posts_bysscat(request, categorie, sscategorie):
    if request.user.is_authenticated():
        return render(request, 'forum/list_posts.html')
    else:
        return render(request, 'intra/index.html')

def add_post(request):
    if request.user.is_authenticated():
        categories = PostCategorie.objects.all()
        sscategories = PostSsCategorie.objects.all()
        cats = PostCategorie.objects.all()
        sscats = PostSsCategorie.objects.all()
        if request.method == 'POST':
            cat = PostSsCategorie.objects.get(name=request.POST['categorie'])
            Post(titre=request.POST['titre'], auteur=request.user.username, categorie=cat).save()
            mypost = Post.objects.get(titre=request.POST['titre'])
            PostMessage(content=request.POST['message'], auteur=request.user.username, post=mypost).save()
        return render(request, 'forum/new.html', locals())
    else:
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
