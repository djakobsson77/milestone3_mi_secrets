from django.contrib import admin
from .models import Game

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ("title", "formatted_price")
    search_fields = ("title",)
    ordering = ("title",)

    def formatted_price(self, obj):
        return f"{obj.price}€"

    formatted_price.short_description = "Price"