from django.shortcuts import render, redirect
from .models import User
from .forms import CreateProfileForm, EditProfileForm
from games_play.game.models import Game
# Create your views here.

def create_profile(request):
    form = CreateProfileForm()

    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    context = {
        'form': form
    }

    return render(request, 'user/create-profile.html', context=context)

def edit_profile(request):
    profile = User.objects.first()
    form = EditProfileForm(instance=profile)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details-profile')

    context = {
        'form': form
    }

    return render(request, 'user/edit-profile.html', context=context)

def details_profile(request):

    profile = User.objects.first()
    current_name = ''
    if profile.first_name:
        current_name += f"{profile.first_name} "
    if profile.last_name:
        current_name += f"{profile.last_name}"
    games = Game.objects.all()
    average_rating = sum([game.rating for game in games])

    context = {
        'profile': profile,
        'current_name': current_name,
        'games': games,
        'average_rating': average_rating
    }

    return render(request, 'user/details-profile.html', context=context)

def delete_profile(request):
    profile = User.objects.first()
    games = Game.objects.all()

    if request.method == 'POST':
        profile.delete()
        games.delete()
        return redirect('home-page')

    return render(request, 'user/delete-profile.html')
