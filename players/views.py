from django.shortcuts import render
from players.models import Player
# Create your views here.


def all_players(request):
    players = Player.objects.all()
    return render(request, 'players/all_players.html', {'players': players})
