from django.contrib import admin
from django.urls import path
from blog import views
from django.views. generic import TemplateView

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
]