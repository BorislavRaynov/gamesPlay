from django.shortcuts import render, redirect
from .models import Game
from .forms import CreateGameForm, EditGameForm, DeleteGameForm
# Create your views here.

def create_game(request):
    form  = CreateGameForm()

    if request.method == 'POST':
        form = CreateGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form
    }

    return render(request, 'game/create-game.html', context=context)

def edit_game(request, game_id):
    game = Game.objects.filter(id=game_id).get()
    form = EditGameForm(instance=game)

    if request.method == 'POST':
        form = EditGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'game': game
    }

    return render(request, 'game/edit-game.html', context=context)

def details_game(request, game_id):
    game = Game.objects.filter(id=game_id).get()

    context = {
        'game': game
    }

    return render(request, 'game/details-game.html', context=context)

def delete_game(request, game_id):
    game = Game.objects.filter(id=game_id).get()
    form = DeleteGameForm(instance=game)

    if request.method == 'POST':
        game.delete()
        return redirect('dashboard')

    context = {
        'form': form,
        'game': game
    }

    return render(request, 'game/delete-game.html', context=context)
