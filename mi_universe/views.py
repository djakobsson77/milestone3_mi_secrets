from django.shortcuts import render, get_object_or_404, redirect
from .models import Island, Character, PirateItem
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import ContactForm
from django.conf import settings

def island_list(request):
    islands = Island.objects.all().order_by("name")

    def get_island(name):
        return next((i for i in islands if i.name == name), None)


    categories = {
        "The Secret of Monkey Island": [
            {"name": "Mêlée Island"}, 
            {"name": "Monkey Island"}
        ],
        "Monkey Island 2 – LeChuck's Revenge": [
            {"name": "Booty Island"},
            {"name": "Phatt Island"},
            {"name": "Scabb Island"},
            {"name": "Dinky Island"}
        ],
        "The Curse of Monkey Island": [
            {"name": "Plunder Island"},
            {"name": "Blood Island"},
            {"name": "Skull Island"}
        ],
        "Escape from Monkey Island": [
            {"name": "Jambalaya Island"},
            {"name": "Lucre Island"}
        ],
        "Tales of Monkey Island": [
            {"name": "Gulf of Melange",
                "sub_islands": [
                    "Boulder Beach",
                    "Brillig Island",
                    "Flotsam Island",
                    "Isle of Ewe",
                    "Jerkbait Islands",
                    "Rock of Gelato",
                ]
            }
        ],
        "Return to Monkey Island": [
            {"name": "Barebones Island"},
            {"name": "Brrr Muda Island"},
            {"name": "Scurvy Island"},
            {"name": "Terror Island"}
        ]
    }

    grouped_islands = []

    for game_title, island_entries in categories.items():
        game_islands = []

        for entry in island_entries:
            island_obj = get_island(entry["name"])
            if not island_obj:
                continue

            # Add sub-islands if present
            if "sub_islands" in entry:
                island_obj.sub_islands = [
                    get_island(sub_name)
                    for sub_name in entry["sub_islands"]
                    if get_island(sub_name)
                ]
            else:
                island_obj.sub_islands = []

            game_islands.append(island_obj)

        grouped_islands.append({
            "game": game_title,
            "islands": game_islands
        })

    return render(request, "mi_universe/island_list.html", {
        "grouped_islands": grouped_islands
    })


def island_detail(request, pk):
    island = get_object_or_404(Island, pk=pk)
    return render(request, "mi_universe/island_detail.html", {"island": island})


def character_list(request):
    characters = Character.objects.all()
    return render(request, "mi_universe/character_list.html", {"characters": characters})


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
    return render(request, "mi_universe/pirateitem_list.html", {"items": items})


def pirateitem_detail(request, pk):
    item = get_object_or_404(PirateItem, pk=pk)
    return render(request, "mi_universe/pirateitem_detail.html", {"item": item})


def home(request):
    return render(request, "mi_universe/home.html")


def about(request):
    return render(request, "mi_universe/about.html")


from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.core.mail import send_mail

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        send_mail(
            "New Contact Form Message",
            f"From: {name}\nEmail: {email}\n\nMessage:\n{message}",
            None,
            ["djakobsson77@gmail.com"],
        )

        return redirect("contact_success")


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "mi_universe/signup.html", {"form": form})