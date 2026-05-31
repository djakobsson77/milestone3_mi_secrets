from django.contrib import admin
from .models import Island, Character, PirateItem


# Register your models here.

admin.site.register(Character)
admin.site.register(PirateItem)


@admin.register(Island)
class IslandAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
