from django.shortcuts import render, get_object_or_404
from .models import Island

# Create your views here.


def island_list(request):
    islands = Island.objects.all()
    return render(request, "mi_universe/island_list.html", {"islands": islands})

def island_detail(request, pk):
    island = get_object_or_404(Island, pk=pk)
    return render(request, "mi_universe/island_detail.html", {"island": island})
