from django.core import serializers
from django.apps import apps
import json

def run():
    MODEL_NAMES = [
        "mi_universe.Island",
        "mi_universe.Character",
        "mi_universe.PirateItem",
    ]

    objects = []

    for model_path in MODEL_NAMES:
        app_label, model_name = model_path.split(".")
        model = apps.get_model(app_label, model_name)
        qs = model.objects.all()
        data = serializers.serialize("json", qs)
        objects.extend(json.loads(data))

    with open("data.json", "w", encoding="utf-8", newline="\n") as f:
        json.dump(objects, f, ensure_ascii=False, indent=2)

    print("Export klar! data.json skapad.")
