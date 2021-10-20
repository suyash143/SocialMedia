from . import models
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
import os
import pytz
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if request.user.is_staff is True:
                return HttpResponse(' 200 {{request.user}} is logged in ')
            else:
                return redirect('/index')
        else:
            messages.info(request, "invalid Credentials")
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')
