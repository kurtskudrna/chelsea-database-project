from django.shortcuts import render
# Create your views here.


def all_players(request):
    return render(request, 'players/index.html')
