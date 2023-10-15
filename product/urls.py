from django.urls import path
from .views import fetchallfood,createfood

urlpatterns = [
    path("allfood/", fetchallfood),
    path("createfood/", createfood)
]