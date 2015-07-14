#-*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def user_logout(request):
    logout(request)
    return render(request, 'intra/index.html', locals())

def user_login(request):
    user = authenticate(username=request.POST['pseudo'], password=request.POST['password'])
    if user:
        login(request, user)
    else:
        error = True
    return render(request, 'intra/index.html', locals())

def user_register(request):
    User.objects.create_user(request.POST['pseudo'], request.POST['email'], request.POST['password'])
    return render(request, 'intra/index.html')

def contact(request):
    if not request.POST['nom'] or not request.POST['message'] or not request.POST['sujet'] or not request.POST['email']:
        messages.add_message(request, messages.ERROR, 'Formulaire incomplet !')
    else:
        message = "Nom: " + request.POST['nom'] + " Message: " + request.POST['message'] 
        send_mail(request.POST['sujet'], message, request.POST['email'], ['roger.clanget@live.fr'], fail_silently=False)
    return render(request, 'intra/index.html')

def home(request):
    """
    if not request.is_secure():
        if getattr(settings, 'HTTPS_SUPPORT', True):
            request_url = request.build_absolute_uri(request.get_full_path())
            secure_url = request_url.replace('http://', 'https://')
            return HttpResponseRedirect(secure_url)
    """
    return render(request, 'intra/index.html')

def test(request):
    return render(request, 'intra/test.html')
