from django.shortcuts import render, get_object_or_404, redirect
from .models import Island, Character, PirateItem
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def island_list(request):
    islands = Island.objects.all().order_by("name")

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

    grouped = []

    for game_title, island_entries in categories.items():
        game_group = {"game": game_title, "islands": []}

        for entry in island_entries:
            island_obj = next((i for i in islands if i.name == entry["name"]), None)

            if not island_obj:
                continue

            if "sub_islands" in entry:
                subs = [i for i in islands if i.name in entry["sub_islands"]]
                game_group["islands"].append({
                    "island": island_obj,
                    "sub_islands": subs
                })
            else:
                game_group["islands"].append({
                    "island": island_obj,
                    "sub_islands": []
                })

        grouped.append(game_group)
    return render(request, "mi_universe/island_list.html", {"grouped": grouped})



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


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        full_message = f"From: {name}\nEmail: {email}\n\nMessage:\n{message}"

        send_mail(
            subject="New contact form message",
            message=full_message,
            from_email="noreply@yourdomain.com",
            recipient_list=["your_email@example.com"],
        )

        messages.success(request, "Your message has been sent. Thank you!")
        return redirect(request.META.get("HTTP_REFERER", "home"))

    return redirect("home")


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "mi_universe/signup.html", {"form": form})