from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
import os
from signup.models import Users
import subprocess

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def index(request):
    template = loader.get_template("index.html")
    context = {}
    return HttpResponse(template.render(context, request))


# compile code in this part
def send(request):
    type = request.GET.get("typename")
    code = request.GET.get("code")
    print(code)
    # print(type)
    if type == "python3":
        os.chdir(BASE_DIR)
        print(code)
        script = "echo \"" + code + "\" > myCode.py" + """
        python3 myCode.py &> result.txt
        """
        os.system("bash -c '%s'" % script)
        f = open("result.txt", "r")
        res = f.read()
        f.close()
        return HttpResponse(res)
    elif type == "python2":
        os.chdir(BASE_DIR)
        print(code)
        script = "echo \"" + code + "\" > myCode.py" + """
        python2 myCode.py &> result.txt
        """
        os.system("bash -c '%s'" % script)
        f = open("result.txt", "r")
        res = f.read()
        f.close()
        return HttpResponse(res)
    elif type == "cpp":
        os.chdir(BASE_DIR)
        # print(code)
        f1 = open('main.cpp', 'w')
        f1.write(code)
        f1.close()
        script = "make"+"""
        ./main &> result.txt"""
        os.system("bash -c '%s'" % script)

        f = open("result.txt", "r")
        res = f.read()
        f.close()
        return HttpResponse(res)
    else:
        return HttpResponse("Please select your Compiler!")


# check login section in thi part and responce
def login(request):
        username1 = request.GET.get("username")
        password1 = request.GET.get("password")
        validate = False
        for user in Users.objects.all():
            if user.username == username1:
                if user.password == password1:
                    validate = True
        template = loader.get_template("index.html")
        context = {"validate": validate}
        return HttpResponse(template.render(context, request))


