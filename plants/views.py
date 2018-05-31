from django.shortcuts import render, get_object_or_404
from .models import Plant, Category


# Create your views here.
def index(request):
    plants = Plant.objects
    plants_ch = plants.filter(category="Chryzantemy doniczkowe")
    plants_by = plants.filter(category="Byliny i trawy")
    plants_ba = plants.filter(category="Kwiaty balkonowe")
    plants_ra = plants.filter(category="Kwiaty rabatowe")
    context = {'chryzantemy': plants_ch,
               'balkonowe': plants_ba,
               'rabatowe': plants_ra,
               'byliny': plants_by}
    return render(request, 'plants/index.html', context)


def detail(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    return render(request, 'plants/detail.html', {'plant': plant})