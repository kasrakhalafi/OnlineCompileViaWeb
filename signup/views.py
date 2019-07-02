from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import os
from .models import Users
import subprocess
import random

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def index(request):
    template = loader.get_template("index2.html")
    context = {}
    return HttpResponse(template.render(context, request))


def signup(request):
    newpass = request.GET.get("password")
    newuser = request.GET.get("username")
    print(newuser)
    for user in Users.objects.all():
        if user.username == newuser:
            print("username Exists")
            return HttpResponse("username Exists")
    # print(BASE_DIR)
    filepath = "{}/users_codes".format(BASE_DIR)+"/{}".format(newuser)
    os.system("mkdir -p {}".format(filepath))
    print(newuser)
    user = Users(username=newuser, password=newpass)
    print(user.username)
    user.save()
    return HttpResponse("user created")


