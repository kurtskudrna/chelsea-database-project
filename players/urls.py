from django.urls import path, include
from players import views


app_name = 'players'

urlpatterns = [
    path('', views.all_players, name='all_players'),
    path('<int:pk>', views.player_detail, name='player_detail'),
]
