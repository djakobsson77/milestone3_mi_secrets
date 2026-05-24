from django.contrib import admin
from .models import Game, CartItem


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "formatted_price")
    search_fields = ("title",)
    ordering = ("title",)
    list_editable = ("price",)

    def formatted_price(self, obj):
        return f"{obj.price}€"

    formatted_price.short_description = "Price"


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    """
    Admin-konfiguration för CartItem-modellen.
    Gör det möjligt att se och administrera kundvagnsposter.
    """
    list_display = ("user", "game", "quantity")
    list_filter = ("user",)
    search_fields = ("user__username", "game__title")
    ordering = ("user",)
