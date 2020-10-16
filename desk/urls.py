from django.contrib import admin
from django.urls import path
from desk import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("/", views.action, name = "action")
]