from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Game

# Create your views here.

@login_required
def shop(request):
    games = Game.objects.all()
    return render(request, "shop/shop.html", {"games": games})
