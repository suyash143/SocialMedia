from django.db import models
from django.contrib.auth import get_user_model
from allauth.account.signals import user_logged_in

def user_logged_in_reciever(request,user,**kwargs):
    print(user)
    print(request)
    print(kwargs)
User=get_user_model()
user_logged_in.connect(user_logged_in_reciever,User)
