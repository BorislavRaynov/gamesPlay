from django.shortcuts import render
from games_play.user.models import User
from games_play.game.models import Game
# Create your views here.
# home_page, dashboard

def home_page(request):
    return render(request, 'common/home-page.html')


def dashboard(request):
    profile = User.objects.first()
    games = Game.objects.all()

    context = {
        'profile': profile,
        'games': games
    }

    return render(request, 'common/dashboard.html', context=context)
