from django.urls import path, include
from players import views

urlpatterns = [
    path('', views.all_players),
]
