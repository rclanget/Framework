#-*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from intra.models import UserLanguage
from django.utils import translation

def user_logout(request):
    logout(request)
    return render(request, 'intra/index.html', locals())

def user_login(request):
    user = authenticate(username=request.POST['pseudo'], password=request.POST['password'])
    if user:
        login(request, user)
        try:
            myuser = UserLanguage.objects.get(user=request.user.username)
            translation.activate(myuser.language)
            messages.add_message(request, messages.SUCCESS, 'Vous êtes connecté')
        except:
            myuser = None
    else:
        error = True
    return render(request, 'intra/index.html', locals())

def user_register(request):
    try:
        User.objects.get(username=request.POST['pseudo'])
    except User.DoesNotExist:
        User.objects.create_user(request.POST['pseudo'], request.POST['email'], request.POST['password'])
        messages.add_message(request, messages.SUCCESS, 'Votre compte a été créé')
    else:
        messages.add_message(request, messages.ERROR, 'Ce pseudo éxiste deja !')
    return render(request, 'intra/index.html')

def contact(request):
    if not request.POST['nom'] or not request.POST['message'] or not request.POST['sujet'] or not request.POST['email']:
        messages.add_message(request, messages.ERROR, 'Formulaire incomplet !')
    else:
        message = "Nom: " + request.POST['nom'] + " Message: " + request.POST['message'] 
        send_mail(request.POST['sujet'], message, request.POST['email'], ['roger.clanget@live.fr'], fail_silently=False)
    return render(request, 'intra/index.html')

def home(request):
    if request.user.is_authenticated():
        language=request.LANGUAGE_CODE
        try:
            user = UserLanguage.objects.get(user=request.user.username)
            user.language = language
            user.save()
        except:
            UserLanguage.objects.create(user=request.user.username, language=language)
    return render(request, 'intra/index.html')
