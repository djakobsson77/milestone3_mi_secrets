from django.urls import path
from . import views

urlpatterns = [
    path("islands/", views.island_list, name="island_list"),
    path("islands/<int:pk>/", views.island_detail, name="island_detail"),
]
