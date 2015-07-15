#-*- coding: utf-8 -*-
from django.db import models

class PostCategorie(models.Model):
    name = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.name

class PostSsCategorie(models.Model):
    name = models.CharField(max_length=100)
    postcategorie = models.ForeignKey('PostCategorie')

    def __unicode__(self):
        return self.name

class Post(models.Model):
    titre = models.CharField(max_length=150)
    auteur = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True, verbose_name="Date de publication")
    sscategorie = models.ForeignKey('PostSsCategorie', null=True)
    categorie = models.ForeignKey('PostCategorie')

    def __unicode__(self):
        return self.titre

class PostMessage(models.Model):
    content = models.TextField(null=True)
    auteur = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post')

    def __unicode__(self):
        return self.content

class Thread(models.Model):
    content = models.TextField(null=True)
    auteur = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    postmessage = models.ForeignKey('PostMessage')

    def __unicode__(self):
        return self.content
    
