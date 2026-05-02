from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("islands/", views.island_list, name="island_list"),
    path("islands/<int:pk>/", views.island_detail, name="island_detail"),
    path("characters/", views.character_list, name="character_list"),
    path("characters/<int:pk>/", views.character_detail, name="character_detail"),
    path("pirateitems/", views.pirateitem_list, name="pirateitem_list"),
    path("pirateitems/<int:pk>/", views.pirateitem_detail, name="pirateitem_detail"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]
