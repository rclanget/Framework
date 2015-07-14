from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from ticket.models import Ticket, Message, Categorie
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib import messages

def reply(request):
    if request.user.is_authenticated():
        myticket = Ticket.objects.get(id=request.POST['id'])
        Message(content=request.POST['message'], auteur=request.user.username, ticket=myticket).save()
        return HttpResponseRedirect(reverse('ticket.views.ticket', kwargs={'t': request.POST['id']}))

def openorclose(request):
    if request.user.is_authenticated():
        myticket = Ticket.objects.get(id=request.POST['id'])
        tickets = Ticket.objects.all()
        if myticket.status:
            Ticket.objects.filter(id=request.POST['id']).update(status=False, closeby=request.POST['username'])
            return render(request, 'ticket/index.html', locals())
        else:
            Ticket.objects.filter(id=request.POST['id']).update(status=True)
            return render(request, 'ticket/index.html', locals())
    return render(request, 'intra/index.html')

def attributeto(request):
    if request.user.is_authenticated():
        Ticket.objects.filter(id=request.POST['id']).update(attributedto=request.POST['user'])
        tickets = Ticket.objects.all()
        return render(request, 'ticket/index.html', locals())
    return render(request, 'intra/index.html')

def new_ticket(request):
    if request.user.is_authenticated():
        categories = Categorie.objects.all()
        if not request.POST['titre'] or not request.POST['message']:
            messages.add_message(request, messages.ERROR, 'Formulaire incomplet !')
        else:
            myauteur = request.user.username
            mycategorie = Categorie.objects.get(name=request.POST['categorie'])
            Ticket(titre=request.POST['titre'], auteur=myauteur, closeby=None, attributedto=None, status=True, categorie=mycategorie).save()
            myticket = Ticket.objects.get(titre=request.POST['titre'])
            Message(content=request.POST['message'], auteur=myauteur, ticket=myticket).save()
            messages.add_message(request, messages.SUCCESS, 'Ticket envoye !')
        return render(request, 'ticket/new.html', locals())
    return render(request, 'intra/index.html')

def add(request):
    if request.user.is_authenticated():
        categories = Categorie.objects.all()
        return render(request, 'ticket/new.html', locals())
    return render(request, 'intra/index.html', locals())

def ticket(request, t):
    if request.user.is_authenticated():
        ticket = Ticket.objects.get(id=t)
        msgs = Message.objects.all()
        users = User.objects.all()
        return render(request, 'ticket/ticket.html', locals())
    return render(request, 'intra/index.html')

def home(request):
    if request.user.is_authenticated():
        tickets = Ticket.objects.all()
        return render(request, 'ticket/index.html', locals())
    return render(request, ('intra/index.html'))
