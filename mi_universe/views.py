from django.shortcuts import render, get_object_or_404, redirect
from .models import Island, Character, PirateItem
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings


def island_list(request):
    islands = Island.objects.all().order_by("game", "name")

    grouped = {}
    for island in islands:
        grouped.setdefault(island.game, []).append(island)

    return render(request, "mi_universe/island_list.html", {
        "grouped_islands": grouped.items()
    })


def island_detail(request, pk):
    island = get_object_or_404(Island, pk=pk)
    return render(
        request, "mi_universe/island_detail.html", {"island": island}
        )


def character_list(request):
    characters = Character.objects.all()
    return render(
        request, "mi_universe/character_list.html", {"characters": characters}
        )


def character_detail(request, pk):
    character = get_object_or_404(Character, pk=pk)

    if character.image_file:
        images = [img.strip() for img in character.image_file.split(",")]
    else:
        images = []

    context = {
        "character": character,
        "images": images,
    }

    return render(request, "mi_universe/character_detail.html", context)


def pirateitem_list(request):
    items = PirateItem.objects.all()
    return render(
        request, "mi_universe/pirateitem_list.html", {"items": items}
        )


def pirateitem_detail(request, pk):
    item = get_object_or_404(PirateItem, pk=pk)
    return render(
        request, "mi_universe/pirateitem_detail.html", {"item": item}
        )


def home(request):
    return render(request, "mi_universe/home.html")


def about(request):
    return render(request, "mi_universe/about.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        send_mail(
            "New Contact Form Message",
            f"From: {name}\nEmail: {email}\n\nMessage:\n{message}",
            settings.DEFAULT_FROM_EMAIL,
            ["djakobsson77@gmail.com"],
        )

        return redirect("contact_success")

    return redirect("/")


def contact_success(request):
    return render(request, "mi_universe/contact_success.html")


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "mi_universe/signup.html", {"form": form})
