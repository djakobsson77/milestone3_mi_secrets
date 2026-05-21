from django.contrib import admin
from .models import Island, Character, PirateItem
from django.contrib.auth.models import User


# Register your models here.

admin.site.register(Character)
admin.site.register(PirateItem)

@admin.register(Island)
class IslandAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

admin.site.unregister(User)

@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "is_staff", "is_active", "date_joined")
    ordering = ("date_joined",)
