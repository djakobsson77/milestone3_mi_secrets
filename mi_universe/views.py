from django.shortcuts import render, get_object_or_404
from .models import Island, Character, PirateItem

def island_list(request):
    islands = Island.objects.all()
    return render(request, "mi_universe/island_list.html", {"islands": islands})


def island_detail(request, pk):
    island = get_object_or_404(Island, pk=pk)
    return render(request, "mi_universe/island_detail.html", {"island": island})


def character_list(request):
    characters = Character.objects.all()
    return render(request, "mi_universe/character_list.html", {"characters": characters})


def character_detail(request, pk):
    character = get_object_or_404(Character, pk=pk)

    # Gör om image_file (sträng) till en lista
    if character.image_file:
        images = [img.strip() for img in character.image_file.split(",")]
    else:
        images = []

    return render(request, "mi_universe/character_detail.html", {
        "character": character,
        "images": images,
    })


def pirateitem_list(request):
    items = PirateItem.objects.all()
    return render(request, "mi_universe/pirateitem_list.html", {"items": items})

def pirateitem_detail(request, pk):
    item = get_object_or_404(PirateItem, pk=pk)
    return render(request, "mi_universe/pirateitem_detail.html", {"item": item})