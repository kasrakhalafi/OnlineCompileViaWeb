from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import os
import subprocess
import random

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def index(request):
    template = loader.get_template("index3.html")
    context = {}
    return HttpResponse(template.render(context, request))


def save(request):
    UserName = request.GET.get("username")
    context = request.GET.get("context")
    codename = request.GET.get("codename")
    type = request.GET.get("type")
    UserName = "mycode"
    if type == "cpp":
        filepath = "{}/users_codes".format(BASE_DIR) + "/{}".format(UserName)
        os.system("touch -p {}.".format(filepath))
        f = open("{}/users_codes".format(BASE_DIR) + "/{}".format(UserName)+codename+".cpp", "a")
        f.close()
    else:
        pass

    return HttpResponse("file saved")
