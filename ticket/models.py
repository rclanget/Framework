from django.db import models

class Message(models.Model):
    content = models.TextField()
    auteur = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True, verbose_name="Date de creation")
    ticket = models.ForeignKey('Ticket')

    def __unicode__(self):
        return self.content

class Categorie(models.Model):
    name = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.name

class Ticket(models.Model):
    titre = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True, verbose_name="Date de creation")
    auteur = models.CharField(max_length=100)
    closeby = models.CharField(max_length=100, null=True)
    attributedto = models.CharField(max_length=100, null=True)
    status = models.BooleanField(default=True)
    categorie = models.ForeignKey('Categorie')

    def __unicode__(self):
        return self.titre
