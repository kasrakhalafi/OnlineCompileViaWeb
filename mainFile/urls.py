from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('send/', views.send),
    path('login/', views.login),

]
