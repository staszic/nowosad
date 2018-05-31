from django.shortcuts import render, get_object_or_404
from .models import Plant, Category


# Create your views here.
def index(request):
    plants = Plant.objects
    plants_ch = plants.filter(category=2).order_by('plant_name')
    plants_by = plants.filter(category=1).order_by('plant_name')
    plants_ba = plants.filter(category=3).order_by('plant_name')
    plants_ra = plants.filter(category=4).order_by('plant_name')
    context = {'chryzantemy': plants_ch,
               'balkonowe': plants_ba,
               'rabatowe': plants_ra,
               'byliny': plants_by}
    return render(request, 'plants/index.html', context)


def detail(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    return render(request, 'plants/detail.html', {'plant': plant})